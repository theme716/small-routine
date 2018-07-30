from bs4 import BeautifulSoup
import requests
from urllib import request

# 发送请求
base_url = 'http://www.itxdl.cn/html/php/PHPvideos/index.html'
response = requests.get(base_url)
response.encoding = response.apparent_encoding


# 显示下载进度的函数
def report(a,b,c):
    per = 100.0*a*b/c
    if per>100:
        per=100
    print('\r%.2f%%'%per,end='')

# 提取信息
if response.status_code == 200:
    html = response.text
    html = BeautifulSoup(html,'lxml') #构建bs4对象
    # 先提取大的模块，组成列表
    video_list = html.select('div.content-kec ul li')
    for video in video_list:
        # 在大的模块里提取各个信息，并重组
        title = video.select('div.tit-l')[0].text.strip().strip('（.')
        href = video.select('a.suoluetu')[0]['href']
        print()
        print('downloading...%s'%href)
        # 下载视频
        request.urlretrieve(href,'./php/'+title+'.mp4',reporthook=report)