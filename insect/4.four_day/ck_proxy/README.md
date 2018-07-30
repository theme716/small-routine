#### 使用代理发送请求的方法
1. urllib 包使用代理
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
# 构建代理管理器，并设置全局opener
proxy_handler = request.ProxyHandler(proxy)
opener = request.build_opener(proxy_handler)
request.install_opener(opener)#设置全局opener


3、正常发送请求，如果没有设置全局opener
则需要使用opener.open()发送请求
```
2. requests 包使代理
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