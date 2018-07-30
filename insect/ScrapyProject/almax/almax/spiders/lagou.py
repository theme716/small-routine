# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import hashlib,re,datetime
from datetime import timedelta
from scrapy_redis.spiders import RedisCrawlSpider

class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    redis_key = 'lagou'
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'almax.mymiddlewares.RandomUserAgentCookie': 998,
        },
        'ITEM_PIPELINES':{
            # 'pro.pipelines.LagouPipeline':1
            'scrapy_redis.pipelines.RedisPipeline':999
        },
        'COOKIES_ENABLED':False,
        'CONCURRENT_REQUESTS' : 32,
        'CONCURRENT_ITEMS' : 32,
    }

    rules = (
        Rule(LinkExtractor(allow=(r'lagou\.com/zhaopin/\w+',),tags=('a',),attrs=('href',)),follow=True),  #首页左侧导航栏入口、列表页下一页入口
        Rule(LinkExtractor(allow=(r'lagou\.com/gongsi/',), tags=('a',), attrs=('href',)), follow=True),  #公司入口、公司详情页社招和校招入口
        Rule(LinkExtractor(allow=(r'lagou\.com/jobs/list_',), tags=('a',), attrs=('href',)), follow=True),  #搜索页快捷搜索入口
        Rule(LinkExtractor(allow=(r'xiaoyuan\.lagou',), tags=('a',), attrs=('href',)), follow=True),  #校招入口
        Rule(LinkExtractor(allow=(r'isSchoolJob',), tags=('a',), attrs=('href',)), follow=True),  #校招列表页
        Rule(LinkExtractor(allow=(r'jobs/\d+\.html',), tags=('a',), attrs=('href',)),callback='parse_item', follow=False),  #详情页
    )


    # 解析详情页
    def parse_item(self, response):
        print(response.status,'------------------]]]]]]]]]]]]]]]]')

        url = response.url
        # url.md5
        url_id = self.md5(url)
        # 职位名称
        pname = response.xpath('//div[@class="job-name"]//span[@class="name"]/text()').extract()[0]
        # 薪资
        money = response.xpath('//dd[@class="job_request"]//span/text()').extract()[0].lower()
        smoney = money.replace('k','').split('-')[0]
        emoney = money.replace('k','').split('-')[1]
        # 工作地点
        location = response.xpath('//dd[@class="job_request"]//span/text()').extract()[1].replace('/','').strip()
        # 经验要求0，为不受限
        allyear = response.xpath('//dd[@class="job_request"]//span/text()').extract()[2]
        allyear = self.parse_year(allyear)
        syear = allyear[0]
        eyear = allyear[1]
        # 学历
        degree = response.xpath('//dd[@class="job_request"]//span[last()-1]/text()').extract()[0].replace('/','').strip()
        # 职位类型
        ptype = response.xpath('//*[@class="job_request"]/p/span[5]/text()').extract()[0]
        tags = response.css('.position-label li::text').extract()
        tags = ','.join(tags)
        # 发布日期
        date_pub = response.css('.publish_time::text').extract()[0]
        date_pub = self.parse_date(date_pub)
        # 职位诱惑
        advantage = response.css('.job-advantage p::text').extract()[0]
        # 职位描述
        jobdesc =  response.css('.job_bt div').extract()

        # 工作详细地址
        jobaddr = response.xpath('//div[@class="work_addr"]//text()').extract()[:-2]
        jobaddr = ''.join(jobaddr).replace('\n','').replace(' ','')
        company = response.css('#job_company dt a img::attr(alt)').extract()[0]
        spider_name = 'lagou'
        # 抓取时间
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')

        item = {
            'url': url,
            'url_id': self.md5(url),
            'pname': pname,
            'smoney': smoney,
            'emoney': emoney,
            'location': location,
            'syear': syear,
            'eyear': eyear,
            'degree': degree,
            'ptype': ptype,
            'tags': tags,
            'date_pub': date_pub,
            'advantage': advantage,
            'jobdesc': jobdesc,
            'jobaddr': jobaddr,
            'company': company,
            'spider_name': spider_name,
            'crawl_time': crawl_time,
        }
        yield item


    def md5(self,value):
        m = hashlib.md5()
        m.update(bytes(value,encoding='utf-8'))
        return m.hexdigest()

    # 处理工作经验的函数
    def parse_year(self,value):
        if '-' in value: #经验1-3年
            num1 = re.findall(r'\d+',value)[0]
            num2 = re.findall(r'\d+',value)[1]
        elif '以下' in value: #经验1年以下
            num1 = 0
            num2 = re.search(r'\d+',value).group()
        elif '以上' in value: #经验几年以上
            num1 = re.search(r'\d+',value).group()
            num2 = 0
        else:  #经验不限
            num1 = 0
            num2 = 0
        return num1,num2

    # 处理时间的函数
    def parse_date(self,value):
        if '天前' in  value:
            num = re.search(r'\d+',value).group()
            date_pub = (datetime.datetime.now()-timedelta(days=int(num))).strftime('%Y-%m-%d')
        elif ':' in value:
            date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        else:
            date_pub = value.split()[0]
        return date_pub
