from urllib import request
import random
'''
http://www.xicidaili.com/ 这个网站有请求头的反爬虫措施，需要构建请求头
'''

# 目标
base_url = 'http://www.xicidaili.com'

# 请求头列表
user_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
]

# 构建请求头
headers = {
    'User-Agent':random.choice(user_list)
}

# 构建请求对象
req = request.Request(url=base_url,headers=headers)

# 发起请求
reponse = request.urlopen(req)

# 获取返回值,并解码为相应的格式
html = reponse.read().decode()

# 将返回值存入文件
with open('xici.html','w',encoding='utf-8') as f:
    f.write(html)
