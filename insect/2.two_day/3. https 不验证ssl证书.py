from urllib import request
import ssl

# 设置默认的ssl验证为，不验证！
ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://www.12306.cn/mormhweb/'
response = request.urlopen(base_url)

print(response.read().decode())


