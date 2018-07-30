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


class BaiheItem(scrapy.Item):

    userID = scrapy.Field() # 用户id
    gender = scrapy.Field() # 性别
    nickname = scrapy.Field() #昵称
    age = scrapy.Field() #年龄
    height = scrapy.Field() # 身高
    educationChn = scrapy.Field() # 教育情况
    marriageChn = scrapy.Field() # 婚否
    incomeChn = scrapy.Field() # 收入情况
    cityChn = scrapy.Field() #城市
    pic_list = scrapy.Field()
    woman_introduce_tag = scrapy.Field() #女方自我标签
    perData_intr = scrapy.Field() #女方自我介绍
    pic_pathurl = scrapy.Field() #图片路径
    one_url = scrapy.Field()

    def get_sql(self):
        sql = 'insert into baihe(userID,gender,nickname,age,height,educationChn,marriageChn,incomeChn,cityChn,woman_introduce_tag,perData_intr,pic_pathurl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [self['userID'],self['gender'],self['nickname'],self['age'],self['height'],self['educationChn'],self['marriageChn'],self['incomeChn'],self['cityChn'],self['woman_introduce_tag'],self['perData_intr'],self['pic_pathurl']]
        return sql,data

