# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import re

class TencentSpider(RedisCrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    # start_urls = ['http://www.baidu.com/']
    redis_key = 'tencent_url'

    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
        },
        'CONCURRENT_REQUESTS': 50,
        'CONCURRENT_ITEMS': 32,
    }

    rules = (
        Rule(LinkExtractor(allow=(r'social.php', r'position.php'), tags=('a',), attrs=('href',)), follow=True),
        Rule(LinkExtractor(allow=(r'position_detail\.php\?id='), tags=('a',), attrs=('href',)), callback='parse_item',
             follow=False)
    )

    def parse_item(self, response):

        title = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        info = response.xpath('//tr[@class="c bottomline"]/td/text()').extract()
        location = info[0]
        ptype = info[1]
        number = info[2]
        number = re.search(r'\d+', number).group()

        item = {
            'title': title,
            'location': location,
            'ptype': ptype,
            'number': number
        }

        yield item
