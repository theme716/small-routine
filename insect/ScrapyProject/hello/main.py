from scrapy.cmdline import execute
import os
os.chdir('hello/spiders')

execute('scrapy runspider liepin.py'.split())
# execute('scrapy crawl liepin'.split())
