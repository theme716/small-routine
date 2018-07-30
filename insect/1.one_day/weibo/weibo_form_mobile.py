from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_handler)

def login():
    base_url = 'https://passport.weibo.cn/sso/login'

    # 构建form数据
    form_data = {
        'username':'ckttty@sina.com',
        'password':'960105LDNsina',
        'savestate': 1,
        'ec': 0,
        'pagerefer': 'https://m.weibo.cn/?jumpfrom=weibocom',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'hff': '',
        'hfp': ''

    }
    form_data = parse.urlencode(form_data).encode()

    # 构建请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom'
    }

    # 构建请求对象
    req = request.Request(base_url,data=form_data,headers=headers)
    # 发送请求:
    response = opener.open(req)
    # print(response.read().decode())

def myhome():
    base_url = 'https://m.weibo.cn/?jumpfrom=weibocom'
    # 构建请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
        # 'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dweibocom'
    }

    # 构建请求对象
    req = request.Request(base_url,headers=headers)
    response = opener.open(req)
    with open('weibo_form_moblie.html','w') as f:
        f.write(response.read().decode('utf-8'))

if __name__=='__main__':
    login()
    myhome()

