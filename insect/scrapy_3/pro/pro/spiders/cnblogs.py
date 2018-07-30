import scrapy
from urllib import request

class cnblogs(scrapy.Spider):

    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']
    base_url = 'https://www.cnblogs.com/'
    def parse(self, response):
        # 发送二级菜单请求（post请求）
        menu_url = 'https://www.cnblogs.com/aggsite/SubCategories'
        body = {"cateIds":"108698,2,108701,108703,108704,108705,108709,108712,108724,4"}
        # body = parse.urlencode(body)
        # 获取菜单
        yield scrapy.FormRequest(url=menu_url,formdata=body,callback=self.menu_list) #发送post请求方法一

    # 解析菜单，每个种类的请求
    def menu_list(self,response):
        a_list = response.xpath('//div[@class="cate_content_block"]//a')
        a_list.reverse() #反转列表
        for a in a_list:
            genre = a.xpath('./text()').extract()[0]
            url = a.xpath('./@href').extract()[0]
            url = request.urljoin(self.base_url,url)
            yield scrapy.Request(url=url,callback=self.genre_num)

    # 解析每个类别有多少页，然后每一页都发送
    def genre_num(self,response):
        total_page = response.xpath('//div[@class="pager"]/a[last()-1]/text()').extract()[0]
        # for i in range(int(total_page),0,-1):
        for i in range(1, 0, -1):
            full_url = response.url+str(i)
            yield scrapy.Request(url=full_url,callback=self.one_fenre)

    # 解析每个列表页（文章列表页）
    def one_fenre(self,response):
        info_list = response.xpath('//div[@id="post_list"]/div')
        for info in info_list:
            title = info.xpath('.//h3/a/text()').extract()[0].strip()
            summary = info.xpath('.//p/text()').extract()[0].strip()
            info_url = info.xpath('.//h3/a/@href').extract()[0].strip()
            yield scrapy.Request(info_url,callback=self.last_parse)

    # 解析详情页（文章页）
    def last_parse(self,response):
        content = response.xpath('//div[@id="cnblogs_post_body"]').extract() #这是文章内容

        # 接下来的工作
        # 将这些内容存入数据库
        # 将图片下载下来，然后看能不能替换成本地的图片名称


