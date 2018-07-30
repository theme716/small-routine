# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentItem
import re

class Tencent2Spider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/']

    custom_settings = {
        'ITEM_PIPELINES':{
            'pro.pipelines.TencentPipeline':1,
        },
        'CONCURRENT_REQUESTS':50,
        'CONCURRENT_ITEMS' : 32,
        'RANDOMIZE_DOWNLOAD_DELAY':True
    }

    rules = (
        Rule(LinkExtractor(allow=(r'social.php',r'position.php'),tags=('a',),attrs=('href',)),follow=True),
        Rule(LinkExtractor(allow=(r'position_detail\.php\?id='),tags=('a',),attrs=('href',)),callback='parse_item',follow=False)

    )

    def parse_item(self, response):
        item = TencentItem()
        title = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        info = response.xpath('//tr[@class="c bottomline"]/td/text()').extract()
        location = info[0]
        ptype = info[1]
        number = info[2]
        number = re.search(r'\d+',number).group()

        item['title'] = title
        item['location'] = location
        item['ptype'] = ptype
        item['number'] = number

        yield item


