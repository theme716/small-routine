import scrapy
from ..items import TeacherItem
class Teacher(scrapy.Spider):
    name = "teacher"
    allowed_domains = [] # 爬虫允许爬取的有效域，限制除了start_urls以外的请求
    start_urls = ['http://www.itxdl.cn/activity/teacher/teacher_lieibiao/']

    def parse(self, response):
        teacher_list = response.css('div.php_jiangshi_liebiao')
        for teacher in teacher_list:

            item = TeacherItem()
            # 提取数据
            name = teacher.xpath('.//h1/text()').extract()[0]
            industry = teacher.xpath('.//p/text()').extract()[0]
            image = teacher.xpath('.//img/@src').extract()[0]
            item['name'] = name
            item['industry'] = industry
            item['image'] = image
            yield item
