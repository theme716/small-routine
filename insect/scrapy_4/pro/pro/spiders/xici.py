import scrapy
from ..items import XiCiItem

class XiCi(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com'] # 爬虫允许爬取的有效域，限制除了start_urls以外的请求
    start_urls = ['http://www.xicidaili.com/nn/1']
    base_url = 'http://www.xicidaili.com/nn/%d'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            # 'pro.mymiddlewares.RandomProxyMysql':899, #这是数据库随机代理的中间件
            'pro.mymiddlewares.RandomUserAgent':900, #这是随机UserAgent的中间件
            # 'pro.mymiddlewares.RandomProxySettings': 999, #这是本机随机代理的中间件
        },
        'ITEM_PIPELINES' : {
            'pro.pipelines.MysqlPipeline':1,
           'pro.pipelines.ProPipeline': 300,
        },
        'RETRY_TIMES': 5,  # 下载器重试次数
        'DOWNLOAD_TIMEOUT': 5,  # 下载器请求超时设置
        'CONCURRENT_REQUEST': 32,  # 并发数
    }

    def parse(self, response):
        for i in range(3265,1,-1):
            full_url = self.base_url%i
        #     构建请求（使用回调函数，启用回调函数，多协程执行）
            yield scrapy.Request(full_url,headers=self.headers,callback=self.parse_page)

    def parse_page(self,response):
        print('==========-----------------下一页-----============]]]]]]]]]]]]]]]]]')
        tr_list = response.xpath('//table//tr')[1:]
        for tr in tr_list:
            item = XiCiItem()
            info = tr.css('td::text').extract()
            host = info[0]
            port = info[1]
            item['host'] = host
            item['port'] = port
            yield item
