from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar() #建立cookie对象
cookie_handler = request.HTTPCookieProcessor(cookie) #构建cookie管理器
opener = request.build_opener(cookie_handler) #构建opener对象



def login():
    # 构造form表单数据
    base_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'

    form_data = {
        'su':'ckttty%40sina.com',
        'sp':'950613LDNsina'
    }
    form_data = parse.urlencode(form_data)

    # 构建请求对象
    req = request.Request(base_url,data=bytes(form_data,encoding='utf-8'))

    response = opener.open(req)

def myhome():
    base_url = 'https://weibo.com/u/2934524783/home'
    response = opener.open(base_url)
    print(response.read().decode('gb2312'))

if __name__ == '__main__':
    login()
    myhome()