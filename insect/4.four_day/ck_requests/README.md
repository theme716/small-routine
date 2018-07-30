#### requests包的使用方法
1. requests get 方法
```
base_url = 'http://www.xicidaili.com'

# 发送请求
resposne = requests.get(base_url,headers=headers,timeout=3)

# 获取分析编码，并设置为默认解码编码
resposne.encoding = resposne.apparent_encoding
# 获取响应码
print(resposne.status_code)
# 获取http响应头
print(resposne.headers)
# 获取响应体 (bytes类型)
print(resposne.content)
# 获取响应体 （str类型）
print(resposne.text)
```
2. requests post 方法
```
base_url = 'http://www.baidu.com'

# form表单提交的数据
data = {
    'username' : 'alice',
    'password' : '123'
}
resposne = requests.post(base_url,data=data,timeout=3)
# 获取分析编码，并设置为默认解码编码
resposne.encoding = resposne.apparent_encoding
# 获取响应码
print(resposne.status_code)
# 获取http响应头
print(resposne.headers)
# 获取响应体 (bytes类型)
print(resposne.content)
# 获取响应体 （str类型）
print(resposne.text)
```
3. 头部信息，proxy方法
```
1、 
proxy = {
    'http' : 'http://103.242.219.243:8080',
    'https' : 'http://103.242.219.243:8080'
}
# 这是需要登录的代理，alice是用户名，123456是密码
# auth_proxy = {
#     'http' : 'alice:123456@120.78.166.84:6666',
#     'https' : 'alice:123456@120.78.166.84:6666'
# }

2、
# 使用代理
resposne = requests.get(base_url,proxies=proxy)
```