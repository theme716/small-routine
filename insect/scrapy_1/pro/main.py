from scrapy import cmdline

# cmdline.execute('scrapy crawl teacher'.split())
# cmdline.execute('scrapy crawl xici'.split())
cmdline.execute('scrapy crawl anjuke'.split())
# cmdline.execute('scrapy crawl anjuke --nolog'.split())
# scrapy crawl teacher --nolog(可以屏蔽到scrapy自己输出的东西)