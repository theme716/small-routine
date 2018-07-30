from scrapy.cmdline import execute
import os

os.chdir('zhilianzhaopin/spiders')

execute('scrapy runspider zhilian.py'.split())
# execute('scrapy crawl zhilian'.split())

