import requests

base_url = 'http://www.baidu.com'
# response = requests.get(base_url)

# 获取编码格式并复制给请求结果（只对response.text有效）
# response.encoding = response.apparent_encoding

#  获取相应体（bytes类型）
# print(response.content)
# 获取相应体（string类型）
# print(response.text)

# 获取响应码
# print(response.status_code)
# 获取相应头
# print(response.headers)


praxy = {
    'http':'http://183.128.240.254:6666',
    'https':'http://183.128.240.254:6666'
}
# 设置请求头 停止请求相应时间 代理地址等等
response = requests.get()


