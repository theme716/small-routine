# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TeacherItem(scrapy.Item):
    name = scrapy.Field()
    industry = scrapy.Field()
    image = scrapy.Field()

class XiCiItem(scrapy.Item):
    host = scrapy.Field()
    port = scrapy.Field()
    
    
class AnjukeItem(scrapy.Item):
    h_name = scrapy.Field()
    h_num = scrapy.Field()
    h_area = scrapy.Field()
    h_level = scrapy.Field()
    h_agent = scrapy.Field()
    h_address = scrapy.Field()
    h_price = scrapy.Field()
    h_info2 = scrapy.Field()
    h_url = scrapy.Field()
    agent_phone = scrapy.Field()
    h_introduce = scrapy.Field()
    h_img_room = scrapy.Field()
    h_img_hx = scrapy.Field()
    h_img_environment = scrapy.Field()
    h_id = scrapy.Field()