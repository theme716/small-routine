from scrapy.cmdline import execute
import os

os.chdir('almax/spiders')

# 开启爬取腾讯招聘
execute('scrapy runspider tencent.py'.split())

# 开启拉勾网爬取
# execute('scrapy runspider lagou.py'.split())

