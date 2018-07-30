# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class YueHuiItem(scrapy.Item):
    age = scrapy.Field() #年龄
    cityName = scrapy.Field() #城市
    degreeName = scrapy.Field() #学历
    districtName = scrapy.Field() #地区
    uid = scrapy.Field() # 用户id
    incomeName = scrapy.Field() # 收入
    industryName = scrapy.Field() #职业
    marriageName = scrapy.Field() #婚否
    nick = scrapy.Field() # 昵称
    full_url = scrapy.Field() # 详情页
    pic_list = scrapy.Field() #图片列表
    introduction = scrapy.Field() # 个人介绍
    pic_pathurl = scrapy.Field() #图片路径保存
    status = scrapy.Field()
    def get_sql(self):
        sql = 'insert into yuehui_user(age,cityName,degreeName,districtName,uid,incomeName,industryName,marriageName,nick,full_url,introduction,pic_pathurl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [self['age'],self['cityName'],self['degreeName'],self['districtName'],self['uid'],self['incomeName'],self['industryName'],self['marriageName'],self['nick'],self['full_url'],self['introduction'],self['pic_pathurl']]
        return sql,data


class HeartItem(scrapy.Item):
    answer = scrapy.Field()
    answered = scrapy.Field()
    question = scrapy.Field()
    typeName = scrapy.Field()
    uid = scrapy.Field()
    qid = scrapy.Field()
    status = scrapy.Field()
    def get_sql(self):
        sql = 'insert into yuehui_heart(answer,answered,question,typeName,uid,qid) VALUES(%s,%s,%s,%s,%s,%s)'
        data = [self['answer'],self['answered'],self['question'],self['typeName'],self['uid'],self['qid']]
        return sql,data