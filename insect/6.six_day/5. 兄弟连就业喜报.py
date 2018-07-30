from bs4 import BeautifulSoup
import requests

base_url = 'http://www.itxdl.cn/activity/jiuyejianbao/'

response = requests.get(base_url)
response.encoding = response.apparent_encoding
html = response.text
html = BeautifulSoup(html)
