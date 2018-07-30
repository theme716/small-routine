from urllib import request,parse
from http import cookiejar

'''
全自动登录思路：
1、构建了opener对象，由opener.open()发送请求
2、opener对象会存储cookie管理器，cookie管理器负责接收cookie并在需要发送的时候发送出去
3、在跳转到主页时,由于cookie管理器里面已经存储了cookie值，所有可以将cookie发出去
'''

cookie = cookiejar.CookieJar() #建立cookie对象
cookie_handler = request.HTTPCookieProcessor(cookie) #返回cookie管理器
opener = request.build_opener(cookie_handler) #构建opener对象

def login():
    base_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018552325436"
    # form数据准备
    form_data = {
        'email':'13546120129',
        'password':'zz123258'
    }
    form_data = parse.urlencode(form_data)
    # 构建请求对象
    req = request.Request(base_url,data=bytes(form_data,encoding='utf-8'))
    # 发送请求
    # response = request.urlopen(req) #构建了opener对象之后，请求将不再由request发送，而是由opener对象发送
    response = opener.open(req)

def gethome():
    base_url = 'http://www.renren.com/966357560'
    # 发送请求
    response = opener.open(base_url)
    print(response.read().decode())

if __name__=='__main__':
    login()
    gethome()

