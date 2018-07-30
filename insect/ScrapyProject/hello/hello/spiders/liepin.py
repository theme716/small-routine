# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import hashlib,re,datetime
from scrapy_redis.spiders import RedisCrawlSpider

class LiepinSpider(RedisCrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    # start_urls = ['https://www.liepin.com/it/']

    redis_key = 'liepin_url'

    rules = (
        Rule(LinkExtractor(allow=(r'imscid=R000000035',),restrict_xpaths=('//ul[@class="sidebar float-left"]',)),follow=True), # 提取link对象中的url ,发出请求到队列，
        Rule(LinkExtractor(allow=(r'/job/\d+',), restrict_xpaths=('//ul[@class="sojob-list"]',)), callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=(r'/a/\d+',), restrict_xpaths=('//ul[@class="sojob-list"]',)), callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=(r'curPage'),restrict_xpaths=('//div[@class="pager"]')),follow=True)
    )

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            'hello.mymiddlewares.RandomUserAgent':950
        },
        'COOKIES_ENABLED':False,
        'CONCURRENT_REQUESTS':32,
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
        },
    }

    def parse_item(self, response):

        if '该职位已结束' not in response.text:
            url = response.url
            url_id = self.md5(url)
            pname = response.xpath('//h1/text()').extract()[0] #职位名称
            money = response.xpath('//p[@class="job-item-title"]/text()|//p[@class="job-main-title"]/text()').extract()[0]
            smoney,emoney = self.parse_money(money) #最低工资和最高工资，转换成了K，如果为0，则为面议
            location = response.xpath('//p[@class="basic-infor"]/span/a/text()|//p[@class="basic-infor"]/span//text()').extract() # 工作地点
            location = ''.join(location).strip()
            date_pub = response.xpath('//p[@class="basic-infor"]/time/text()').extract()[0] #发布时间
            date_pub = self.parse_date(date_pub)
            degree = response.xpath('//div[@class="job-qualifications"]/span[1]/text()|//div[@class="resume clearfix"]/span[1]').extract()[0] #学历
            company = response.xpath('//div[@class="company-logo"]/p//text()|//p[@class="company-name"]/text()').extract()[0] #公司
            pyear = response.xpath('//div[@class="job-qualifications"]/span[2]/text()|//div[@class="resume clearfix"]/span[2]').extract()[0]
            syear,eyear = self.parse_year(pyear) #工作经验时间
            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')  #采集时间
            spider_name = 'liepin'
            planguage = response.xpath('//div[@class="job-qualifications"]/span[3]/text()|//div[@class="resume clearfix"]/span[3]').extract()[0]  # 语言
            ages = response.xpath('//div[@class="job-qualifications"]/span[4]/text()|//div[@class="resume clearfix"]/span[4]').extract()[0] #年龄限制
            # 注意 planguage 和 ages 拉钩数据库里都没有
            advantage = response.xpath('//div[@class="tag-list"]/span/text()').extract() # 职位诱惑
            advantage = ','.join(advantage)
            ptype = ''
            # 职位描述
            jobdesc = response.xpath('//div[@class="job-item main-message job-description"]|//div[@class="job-main job-description main-message"]').extract()[0]
            if '/a/' not in url:
                jobaddr = response.xpath('//ul[@class="new-compintro"]/li/text()').extract()
                if len(jobaddr) == 3:
                    jobaddr = jobaddr[2]
                else:
                    jobaddr = ''
            else:
                jobaddr = ''

            item = {
                'url':url,
                'url_id':url_id,
                'pname':pname,
                'smoney':smoney,
                'emoney':emoney,
                'location':location,
                'date_pub':date_pub,
                'degree':degree,
                'company':company,
                'syear':syear,
                'eyear':eyear,
                'crawl_time':crawl_time,
                'spider_name':spider_name,
                'planguage':planguage,
                'ages':ages,
                'advantage':advantage,
                'ptype':ptype,
                'jobdesc':jobdesc,
                'jobaddr':jobaddr
            }
            print('===================================================',url)
            yield item
        else:
            print('遇上了一个结束的职位',response.url,'=================================================')



    def md5(self,value):
        m = hashlib.md5()
        m.update(bytes(value,encoding='utf-8'))
        return m.hexdigest()

    def parse_money(self,value):
        if '-' in value:
            money = re.findall('\d+',value)
            smoney = int(int(money[0])*10/12)
            emoney = int(int(money[1])*10/12)
        else:
            smoney = 0
            emoney = 0
        return smoney,emoney

    def parse_year(self,value):
        if '以上' in value:
            syear = re.search('\d+',value).group()
            eyear = 0
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def parse_date(self,value):
        if '-' in value:
            date_pub = value
        else:
            date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        return date_pub
