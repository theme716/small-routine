import requests
from urllib import request
import re

# 会话保持，可以跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
session = requests.session()

def login():
    login_url = 'https://accounts.douban.com/login'
    form = {
        'form_email':'ckttty@sina.com',
        'form_password':'950613ck'
    }
    response = session.post(login_url,data=form)
    response.encoding = response.apparent_encoding
    html =  response.text
    if 'captcha_image' in html:#有验证码
        captcha_image = re.compile(r'id="captcha_image" src="(.+?)"')
        res = captcha_image.search(html)
        captcha = res.group(1)
        request.urlretrieve(captcha,'douban.png')
        # 找到表单中的id
        id_pat = re.compile(r'name="captcha-id" value="(.+?)"')
        res = id_pat.search(html)
        captcha_id = res.group(1)
        print(captcha,captcha_id)

        captcha = input('请输入验证码：')
        form['captcha-solution'] = captcha
        form['captcha-id'] = captcha_id

        response = session.post(login_url,data=form)
        response.encoding = response.apparent_encoding
        html = response.text
        if '个人主页' in html:
            home_url = "https://www.douban.com/mine/"
            response = session.get(home_url)
            response.encoding = response.apparent_encoding
            print('登录成功')
            print(response.url)
            return response
    else:
        print('登录成功')
# 修改签名
def update_sign(response,sign):
    update_sign_url = response.url + 'edit_signature'
    update_sign_url = update_sign_url.replace('/people/','/j/people/')
    html = response.text
    ck_pat = re.compile(r'name="ck" value="(.+?)"')
    res = ck_pat.search(html)
    ck = res.group(1)
    forms= {
        'ck':ck,
        'signature':sign
    }
    response_sign = session.post(update_sign_url,data=forms)
    response_sign.encoding = response_sign.apparent_encoding
    print(response_sign.text)


if __name__ == '__main__':
    response = login()
    if  response:
        while True:
            print('输入"q"退出程序')
            print('输入"1"更改签名')
            choice = input('请输入：')
            if choice == '1':
                sign = input('请输入新的签名：')
                update_sign(response,sign)
            elif choice == 'q':
                break