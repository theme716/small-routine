import requests,re,time

base_url = 'http://live.sina.com.cn/zt/f/v/finance/globalnews1'
response = requests.get(base_url)
response.encoding = response.apparent_encoding
html = response.text
# print(html)

news_pat = re.compile(r'class="bd_i_time_c">(.+?)</p>.+?class="bd_i_txt_c">(.+?)</p>',re.S)
news = news_pat.findall(html)
for new in news:
    print(new)


