# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 腾讯招聘的管道
class TencentItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    ptype = scrapy.Field()
    number = scrapy.Field()

    def get_sql(self):
        sql = 'insert into tencent(location,title,ptype,number) VALUES(%s,%s,%s,%s)'
        data = (self['location'],self['title'],self['ptype'],self['number'])
        return sql,data

class LagouItem(scrapy.Item):
    url = scrapy.Field()  # 职位详情链接
    url_id = scrapy.Field()  # MD5的url
    pname = scrapy.Field()  # 职位名称
    smoney = scrapy.Field()  # 最低工资
    emoney = scrapy.Field()  # 最高工资
    location = scrapy.Field()  # 地区
    syear = scrapy.Field()  # 工作年限最低
    eyear = scrapy.Field() # 工作最高年限
    degree = scrapy.Field()  # 学历
    ptype = scrapy.Field()  # 职位类型
    tags = scrapy.Field()  # 标签
    date_pub = scrapy.Field()  # 发布日期
    advantage = scrapy.Field()  # 职位诱惑
    jobdesc = scrapy.Field()  # 职位简介
    jobaddr = scrapy.Field()  # 工作详细地址
    company = scrapy.Field()  # 公司
    spider_name = scrapy.Field()
    crawl_time = scrapy.Field()  # 抓取时间

    def get_sql(self):
        sql = 'insert into lagou_job(url,url_id,pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company,spider_name,crawl_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [self['url'],self['url_id'],self['pname'],self['smoney'],self['emoney'],self['location'],self['syear'],self['eyear'],self['degree'],self['ptype'],self['tags'],self['date_pub'],self['advantage'],self['jobdesc'],self['jobaddr'],self['company'],self['spider_name'],self['crawl_time']]
        return sql,data
