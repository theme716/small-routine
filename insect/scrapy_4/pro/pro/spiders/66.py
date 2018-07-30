import scrapy
from ..items import XiCiItem

class SixSix(scrapy.Spider):

    name = '66'
    allowed_domains = ['66ip.cn']  # 爬虫允许爬取得有效域，限制除了start_urls以外的请求
    start_urls = ['http://www.66ip.cn/1.html']
    base_url = 'http://www.66ip.cn/%d.html'

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
             # 'pro.mymiddlewares.RandomProxyMysql':899, #这是数据库随机代理的中间件
            'pro.mymiddlewares.RandomUserAgent':900, #这是随机UserAgent的中间件
            # 'pro.mymiddlewares.RandomProxySettings': 999, #这是本机随机代理的中间件
        },
        'RETRY_TIMES' : 5, # 下载器重试次数
        'DOWNLOAD_TIMEOUT' : 3, # 3秒以后请求超时
        'CONCURRENT_REQUEST' : 32, #并发数
        'ITEM_PIPELINES' : {
            'pro.pipelines.MysqlPipeline':1, #管道注册 （存入数据库）
        }
    }

    def parse(self, response):
        for i in range(1290, 0, -1):
            fullurl = self.base_url % i

            # 构建请求
            # callback 回调函数，当下载完成时被调用
            req = scrapy.Request(fullurl, callback=self.parse_page)

            # 把请求通过引擎和调度器放入队列
            yield req

    # 分页请求的处理函数
    def parse_page(self, response):
        print('==========-------------------下一页---============]]]]]]]]]]]]]]]]]')
        proxy_list = response.xpath('//table[last()]//tr')[2:]
        for proxy in proxy_list:
            item = XiCiItem()

            info = proxy.css('td::text').extract()
            host = info[0]
            port = info[1]

            # 填充数据
            item['host'] = host
            item['port'] = port

            yield item

