from urllib import request

# 确定目标
base_url = 'http://www.baidu.com'

# 发起http请求，返回类文件对象
response = request.urlopen(url=base_url)

# 获取响应内容
html = response.read()

# 将相应内容写入文件保存
with open('baidu2.html','w',encoding='utf-8') as f:
    f.write(html.decode('utf-8'))