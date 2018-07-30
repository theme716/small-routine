import scrapy,random
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Boss(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    # start_urls = ['https://www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100-p100109/']
    rules = {
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="job-menu"]/dl[1]//a',)),follow=True),
        Rule(LinkExtractor(allow=(r'page',),restrict_xpaths=('//div[@class="page"]',)),follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="filter-box"]',)),follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="job-list"]/div[1]',)),follow=True),
        Rule(LinkExtractor(allow=(r'/job_detail/',)),callback='parse_item',follow=False),
    }
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'bosszhipin.mymiddlewares.RandomUserAgent': 950,
            'bosszhipin.mymiddlewares.RandomProxySettings':960,
            'bosszhipin.mymiddlewares.ReturnRequest':970,
        },
        'COOKIES_ENABLED': False,
        'RETRY_TIMES':10,
        'DOWNLOAD_DELAY':random.random()*1,
        'CONCURRENT_REQUESTS':1,
        'RETRY_HTTP_CODES':[500, 502, 503, 504, 400, 408,403,302],
    }
    def parse_item(self,response):
        print(response.url)