from urllib import request,parse
import time,random,json

import hashlib
def my_md5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding='utf-8'))
    res = md5.hexdigest()
    return res

def fanyi(kw):
    base_dir = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = str(int(time.time()*1000)+int(random.random()*10))
    sign = 'fanyideskweb' + kw + salt + 'ebSeFb%=XZ%T[KZ)c(sy!'
    forms = {
        "i":kw,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":salt,
        "sign":my_md5(sign),
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false",
    }
    forms = parse.urlencode(forms)
    headers = {
        "Host":"fanyi.youdao.com",
        "Connection":"keep-alive",
        "Content-Length":len(forms),
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Origin":"http://fanyi.youdao.com",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Referer":"http://fanyi.youdao.com/",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"OUTFOX_SEARCH_USER_ID=193202622@10.169.0.84; JSESSIONID=aaaQcQWYyI5d9eWut60pw; OUTFOX_SEARCH_USER_ID_NCOO=1926836278.3461666; fanyi-ad-id=44881; fanyi-ad-closed=1; ___rl__test__cookies=1528822367549",
    }

    req = request.Request(base_dir,data=bytes(forms,encoding='utf-8'),headers=headers)
    response = request.urlopen(req)
    data = response.read().decode()
    data = json.loads(data)
    print('')
    if 'translateResult' in data:
        print('--'+data['translateResult'][0][0]['src']+'>>>'+data['translateResult'][0][0]['tgt'])
        print('')
    if 'smartResult' in data:
        for x in data['smartResult']['entries'][:-1]:
            if x != '':
                print(x)
        print('========================================')
    # print(data)





if __name__ == '__main__':
    while True:
        print('输入"q"退出程序')
        kw = input('请输入翻译内容:')
        if kw  == 'q':
            break
        fanyi(kw)
