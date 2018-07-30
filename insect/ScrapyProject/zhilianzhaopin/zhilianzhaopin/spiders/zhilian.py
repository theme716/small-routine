import scrapy,requests,json,jsonpath,re,hashlib,datetime
from urllib import request
from time import strftime,strptime
from scrapy_redis.spiders import RedisSpider

class zhilian(RedisSpider):

    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['https://www.zhaopin.com/']
    redis_key = 'zhilianzhaopin'

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'zhilianzhaopin.mymiddlewares.RandomUserAgent': 950
        },
        'COOKIES_ENABLED': False,
        'CONCURRENT_REQUESTS': 32,
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
        },
        'RETRY_TIMES': 5,  # 下载器重试次数
    }
    def parse(self, response):
        # 获得要爬取的分类的名称
        type_list = response.xpath('//li[@class="zp-jobNavigater-item"]')

        base_url = 'https://fe-api.zhaopin.com/c/i/sou?start=%d&pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3'

        #获得了一个列表，里面是各种分类名称
        one_type_list = type_list[0].xpath('.//a/text()').extract() #第0个是互联网IT分类的
        print(one_type_list)
        for ptype in one_type_list:
            type_url = base_url.format(ptype)

            # # 分发某一个类别的所有json请求
            response = requests.get(type_url%0)
            data = response.text
            data = json.loads(data)
            numFound = jsonpath.jsonpath(data,'$..numFound')[0]
            for num in range(0,numFound,60):
                yield scrapy.Request(url=type_url%num,callback=self.parse_json)


    # 解析返回的json数据
    def parse_json(self,response):
        data = json.loads(response.text)
        data = data['data']['results']
        # print('==============================================================',len(data),response.url,data)
        # print(response.url,jsonpath.jsonpath(data,'$..positionURL'))

        for one_data in data:
            url = one_data['positionURL']
            url_id = self.md5(url)
            pname = one_data['jobName'] #职位名称
            money = one_data['salary']
            smoney = self.parse_money(money)[0]
            emoney = self.parse_money(money)[1]
            company = one_data['company']['name'] #公司名称
            syear,eyear = self.parse_year(one_data['workingExp']['name']) #工作经验年限
            degree = one_data['eduLevel']['name'] #学历
            ptype = one_data['emplType'] # 工作类型（兼职，全职）
            location = one_data['city']['display'] #工作地区
            advantage = ','.join(one_data['welfare']) #职位诱惑
            tags = one_data['jobType']['display'] # 工作标签
            date_pub = one_data['createDate']
            date_pub = strptime(date_pub,'%Y-%m-%d %H:%M:%S')
            date_pub = strftime('%Y-%m-%d',date_pub)  #发布时间
            spider_name = 'zhilian'     # 爬虫名
            crawl_time = datetime.datetime.now().strftime('%Y-%m-%d') #抓取时间


            item = {
                'url': url,
                'url_id': url_id,
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
                'company': company,
                'spider_name': spider_name,
                'crawl_time': crawl_time,
            }
            yield scrapy.Request(url=url,callback=self.parse_job,meta={'item':item})

    # 解析详情页
    def parse_job(self,response):
        item = response.meta['item']

        jobdesc = response.xpath('//div[@class="tab-inner-cont"]//text()').extract()
        jobdesc = ''.join(jobdesc)
        n = jobdesc.find('工作地址')
        jobdesc = jobdesc[:n]
        jobaddr = response.xpath('//h2//text()').extract()
        if jobaddr:
            if len(jobaddr[1]) >5:
                jobaddr = jobaddr[1]
            else:
                jobaddr = jobaddr[2]
            jobaddr = jobaddr.strip()
        else:
            jobaddr = ''

        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        print(response.url)
        yield item

    def md5(self,value):
        m = hashlib.md5()
        m.update(bytes(value,encoding='utf-8'))
        return m.hexdigest()

    # 处理工作年限
    def parse_year(self,value):
        if '-' in value:
            syear = re.findall('\d+',value)[0]
            eyear = re.findall('\d+',value)[1]
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def parse_money(self,value):
        if '-' in value:
            smoney = value.replace('K','').split('-')[0]
            emoney = value.replace('K','').split('-')[1]
        else:
            smoney = 0
            emoney = 0
        return smoney,emoney

