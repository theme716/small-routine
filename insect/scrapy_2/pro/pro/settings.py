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