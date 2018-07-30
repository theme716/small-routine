# ==================================================spiders/baihe.py====================================================
'''
目标：练习使用数据库存储，下载图片，多个管道处理item
'''
import scrapy,re,json
from .. settings import COOKIE
from ..items import BaiheItem

class baihe(scrapy.Spider):
    name = 'baihe'
    allowed_domains = []
    start_urls = ['http://www.baidu.com']

    id_list = 'http://search.baihe.com/Search/getUserID?&jsonCallBack=jQuery18304023144646136796_1530003036835&page={}'
    friend_list_url = 'http://search.baihe.com/search/getUserList?userIDs={}&jsonCallBack=jQuery18304023144646136796_1530003036837'
    friend_url = 'http://profile1.baihe.com/?oppID={}'

    headers = {
        "Connection": "keep-alive",
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://search.baihe.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://search.baihe.com/",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    json_pat = re.compile(r'\{.+\}',re.S)


    def parse(self, response):
        '''
        :param response:没有用的，百度请求的response
        :return: 返回一个获取用户id json的任务
        '''
        print(response.status)
        for i in range(2,0,-1):
            full_url = self.id_list.format(i)
            yield scrapy.Request(url=full_url,callback=self.get_id,headers=self.headers,cookies=COOKIE)

    def get_id(self,response):
        '''
        :param response: 用户id json文件
        :return: 返回值是一个获得用户信息的json文件，内有多个用户信息
        '''
        # 处理json,结果为一个列表
        data = response.text
        data = self.json_pat.search(data).group()
        data = json.loads(data)
        data = data['data'] # 一个有着各种id的列表

        for i in range(0,len(data),8):
            ids = ','.join(data[i:i+8])
            full_url = self.friend_list_url.format(ids)
            print(full_url)
            yield scrapy.Request(url=full_url,callback=self.friend_json,headers=self.headers,cookies=COOKIE)

    def friend_json(self,response):
        data = response.text
        data = self.json_pat.search(data).group()
        # data = data.encode('gbk')
        data = json.loads(data)
        data = data['data']
        for friend in data: # friend是一个一个字典
            item = BaiheItem()
            item['userID'] = friend['userID']
            item['gender']= friend['gender']
            item['nickname'] = friend['nickname']
            item['age'] = friend['age']
            item['height'] = friend['height']
            item['educationChn'] = friend['educationChn']
            item['marriageChn'] = friend['marriageChn']
            item['incomeChn'] = friend['incomeChn']
            item['cityChn'] = friend['cityChn']
            full_url = self.friend_url.format(friend['userID'])
            item['one_url'] = full_url
            yield scrapy.Request(url=full_url,callback=self.friend,headers=self.headers,cookies=COOKIE,meta={'item':item})

    def friend(self,response):
        '''
        :param response: 提取女朋友个人主页信息
        :return:
        '''
        item = response.meta['item']
        pic_list = response.css('div.big_pic ul img::attr(src)').extract() # 照片路径列表
        woman_introduce_tag = ','.join(response.xpath('//div[@class="womanData"]/div[@class="inter label"]//span/text()').extract()) # 自我标签
        perData_intr = response.xpath('//div[@class="perData"]//div[@class="intr"]/text()').extract()[0].strip() #个人介绍
        # print(pic_list,woman_introduce_tag,perData_intr)
        item['pic_list'] = pic_list
        item['woman_introduce_tag'] = woman_introduce_tag
        item['perData_intr'] = perData_intr

        yield item

# ==================================================items.py============================================================
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


# ==================================================pipelines.py========================================================
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import json,pymysql

class ProPipeline(object):
    def process_item(self, item, spider):
        return item
# 自定义的保存图片的管道，添加了往item中添加图片名字段的功能
class BaiheImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        pic_pathurl = []
        for res in results:
            if res[0]:#下载成功
                pic_pathurl.append(res[1]['path'].strip('full/'))
                print(res[1]['path'])
        pic_pathurl = ','.join(pic_pathurl)
        item['pic_pathurl'] = pic_pathurl
        return item

# 保存入数据库的管道
class BaiheMysqlPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
        self.cursor = self.con.cursor()
    def process_item(self,item,spider):
        sql,data = item.get_sql()
        try:
            self.cursor.execute(sql,data)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print('============================报错===========================')
            print(e)
            print('=============================='+item["one_url"]+'=============================')

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()

# =================================================settings.py==========================================================
# -*- coding: utf-8 -*-

# Scrapy settings for pro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pro'

SPIDER_MODULES = ['pro.spiders']
NEWSPIDER_MODULE = 'pro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pro (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
CONCURRENT_ITEMS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pro.middlewares.ProSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pro.middlewares.ProDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy.pipelines.images.ImagesPipeline':1, #系统默认的图片下载管道
    'pro.pipelines.BaiheImagesPipeline':1,
    'pro.pipelines.BaiheMysqlPipeline':2,
    'pro.pipelines.ProPipeline': 300,
}

# 指定图片字段,这个字段需要和item里面存放图片链接的字段相同，且该字段存储列表
IMAGES_URLS_FIELD = 'pic_list'
# 获取图片路径
import os
Base_dir = os.path.dirname(os.path.dirname(__file__))
# 下载路径
IMAGES_STORE = os.path.join(Base_dir,'images')


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


COOKIE = {
    "accessID":"20180626163703544601",
    "channel":"baidu-pp",
    "code":"350002-001",
    "lastLoginDate":"Tue%20Jun%2026%202018%2016%3A37%3A03%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29",
    "cookie_pcc":"%7C%7Cbaidu-pp%7C%7C350002-001%7C%7Chttps%3A//www.baidu.com/s%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E7%2599%25BE%25E5%2590%2588%25E7%25BD%2591%26oq%3D%2525E7%2525BD%252591%2525E6%252598%252593%2525E4%2525BA%2525A4%2525E5%25258F%25258B%26rsv_pq%3Dc5e0f1f1000228dd%26rsv_t%3Dbac8Rr%252BojIWP0tPlYjjjUsPOu0RkzpMjF3EDspMlmVgMdEw1lEGf7YfErjs%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D13%26rsv_sug1%3D11%26rsv_sug7%3D101%26bs%3D%25E7%25BD%2591%25E6%2598%2593%25E4%25BA%25A4%25E5%258F%258B",
    "tempID":"6624388894",
    "accessToken":"BH1530002224733500112",
    "NTKF_T2D_CLIENTID":"guestFC379E50-E739-0DDC-C739-3B3D392AD642",
    "tongjiType":"noCookie",
    "Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d":"1530002224,1530002400",
    "AuthCookie":"4BFFD62B611D896E3198CF6F337AE22B7605C7AD5509BA2BDD65FCCDDBBE90D5F8F165385F9277B667636D2B7F48C499317452EAB3D472B59BF608CB30C4F468740A0A3FA06C20993BE1E578DAD7F80581A7AEE531573AB6",
    "AuthMsgCookie":"FA1B0EE0455557B92FF9181C3E14E20FA74D5B7162396B7320DE23056CE074D8A69D2B6EAA70CFFFB5FD33BBF208C5B75939D2DE89F6BC6505CE86A00D7CBDFE3FF205599B33C99EE79EC25D2E734C9603940A7DB3A2A8F8",
    "GCUserID":"158463552",
    "OnceLoginWEB":"158463552",
    "LoginEmail":"15313560160%40mobile.baihe.com",
    "userID":"158463552",
    "spmUserID":"158463552",
    "__asc":"d55ff0fe1643b438fbe76a237f7",
    "__auc":"d55ff0fe1643b438fbe76a237f7",
    "orderSource":"10130301",
    "nTalk_CACHE_DATA":"{uid:kf_9847_ISME9754_158463552,tid:1530002225449841}",
    "hasphoto":"1",
    "noticeEvent_158463552":"26",
    "Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d":"1530002864",
    "_fmdata":"%2FPENo7oWISQncNsEEgyozyredZW3PAOMJiJg%2BhUcsjzyDM04yAlgvx9%2Fmov%2FsNikq8KzJfS5BUwC2GxkjYrZe8wbcMxBHEJkz3wi%2BkUEMV4%3D",
    "AuthCheckStatusCookie":"CD2D7B8445D0C4B30382F8B563DB93CC14D1D3015978705726A127B203C4931405E9D878DCC812E7"
}