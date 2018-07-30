from urllib import request,parse
import random

'''
发送带有参数的请求：
1、参数字典需要用parse.urlencode(dict)编码成Unicode码，然后加到url上
'''

qs = {
    'wd':'妹子',
}
qs = parse.urlencode(qs)
base_url = 'http://www.baidu.com/s?'+qs


# 构造请求对象
req = request.Request(base_url)

# 发送请求
response = request.urlopen(req)

print(response.read().decode())