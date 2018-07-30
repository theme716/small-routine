import scrapy
from scrapy.conf import settings

class MiddleTest(scrapy.Spider):
    name = 'middletest'
    allowen_domains = []
    start_urls = ['https://www.baidu.com']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            # 'pro.mymiddlewares.Middle1':1,
            # 'pro.mymiddlewares.Middle2':2,
            # 'pro.mymiddlewares.RandomUserAgent':3,
            'pro.mymiddlewares.RandomProxySettings':999,
        },
        # 'DEFAULT_REQUEST_HEADERS':{
        #     'User-Agent':'这是custom_settings中的头'
        # }
        'RETRY_TIMES':5, # 下载器重试次数
        'DOWNLOAD_TIMEOUT':5 # 下载器请求超时设置
    }

    def parse(self, response):
        print('============================================')
        print(response.request.headers) # response对象中有request对象
        url = 'https://www.taobao.com'
        yield scrapy.Request(url=url,callback=self.parse_list)

    def parse_list(self,response):
        print('==================2==========================')
        print(response.request.headers)