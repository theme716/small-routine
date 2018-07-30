# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor #提取网页中的超链接的类
from scrapy.spiders import CrawlSpider, Rule # 将提取到的链接，构成请求，加入队列的类


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com','baidu.com']
    start_urls = ['http://hr.tencent.com/']

    rules = (
        # 正则匹配
        # Rule(LinkExtractor(allow=(r'position_detail\.php\?id',)), callback='parse_item', follow=False),

        # 正则匹配，并配备请求头,并修饰请求url
        # Rule(LinkExtractor(allow=(r'position_detail\.php\?id',)),process_request='parse_request',process_links='parse_link',callback='parse_item',follow=False),

        # xpath匹配，只匹配spath限定里面的链接
        # Rule(LinkExtractor(restrict_xpaths=('//div[@id="hzhiwei"]',)),callback='parse_item',follow=False),

        # xpath匹配，正则匹配同时使用
        # Rule(LinkExtractor(restrict_xpaths=('//div[@id="home_l"]',),allow=(r'position.php',)),callback='parse_item',follow=False),

        # css匹配
        Rule(LinkExtractor(restrict_css=('div#hzhiwei')),callback='parse_item',follow=False),
    )
    '''
    Rule()的参数：
        link_extractor：一个LinkExtractor()对象
        callback=None：回调函数,解析出来的url，向这个url发出请求之后，处理获得的相应的函数
        cb_kwargs=None
        follow=None：是否递归匹配
        process_links=None 发起请求前，对该url进行处理的函数，返回值是一个url，是一个字符串
        process_request=identity 自定义request规则的函数，返回request对象,是一个字符串
        
    LinkExtractor()的参数:
        allow=() 是一个元组，里面写正则匹配链接的规则,多个规则之间是 '或'
        deny=()
        allow_domains=() 
        deny_domains=()
        restrict_xpaths=() 是一个元组，里面写xpath匹配链接的规则
        restrict_css=() 是一个元祖，里面写css匹配链接的规则
        tags=('a', 'area') 是一个元组，里面写匹配的标签
        attrs=('href',) 是一个元组，里面写匹配标签的什么属性
        canonicalize=False 
        unique=True
        process_value=None 
        deny_extensions=None
        strip=True
    '''
    # 处理发送的请求的函数
    def parse_request(self,request):
        request.dont_filter = True #不过滤重复的url
        request.headers['User-Agent'] = 'User-Agent:Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'
        return request
        # yield scrapy.Request(dont_filter=True)

    # 处理link的函数
    def parse_link(self,links):
        # print(links)
        '''
        这是个Link对象列表，存储了这个tag的各种信息
        [Link(url='https://hr.tencent.com/position_detail.php?id=42007', text='15851-游戏Android高级开...', fragment='', nofollow=False).....]
        '''
        for link in links:
            link.url = 'https://www.baidu.com'
        return links

    # 处理response
    def parse_item(self, response):
        print(response.url)
        # print(response.request.headers['User-Agent'])
