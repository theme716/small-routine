from urllib import request,parse

def gethomt():
    base_url = 'http://www.renren.com/966357560'

    # 构建请求头
    headers = {
        'Cookie': 'anonymid=ji61bejw-ubzey8; depovince=GW; _r01_=1; JSESSIONID=abcEWdLKlgSdG4uD3RFpw; ick_login=dc79f12f-f1a7-40ee-ba47-57cfc150cd10; ick=fd3a2184-6ff8-4d1a-8089-12f8cfdfdc1d; __utma=151146938.769597806.1528466224.1528466224.1528466224.1; __utmc=151146938; __utmz=151146938.1528466224.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; XNESSESSIONID=155c04be46b1; jebe_key=4eed5e98-fc30-4617-835a-745a05a587ee%7C9bbec148653ed9de3a910b6bf469cf51%7C1528466628306%7C1%7C1528466628010; vip=1; first_login_flag=1; ln_uact=13546120129; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=0303abe4-1406-43d6-8aca-00b2764425af|||||; _de=388E13F9289A44C0F7DC708369CBDF64; p=f6bc2aad199de7c856452cf544f357f00; t=d32e9e5615e587336bd74b18dcc9d3290; societyguester=d32e9e5615e587336bd74b18dcc9d3290; id=966357560; xnsid=1feb40d3; loginfrom=syshome'
    }
    # 构建请求对象
    req = request.Request(base_url,headers=headers)
    # 发送请求
    response = request.urlopen(req)

    print(response.read().decode())

if __name__=='__main__':
    gethomt()

