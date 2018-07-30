from urllib import request,parse
import json

'''
目标：对百度翻译页面发送post请求，获得翻译的结果
0、form表单提交的数据，首先需要parse.urlencode()转码，转换成unicode编码格式的字符串，然后装换成utf-8的bytes格式编码
2、如果请求对象里面有data属性，则为发送post请求的请求
'''

# 翻译函数：
def fanyi(kw):

    base_url = 'http://fanyi.baidu.com/sug'

    # 1、 form表单数据准备
    form_data = {
        'kw':kw
    } # 构造请求的表单数据（post请求发送的东西）
    form_data = parse.urlencode(form_data) # 对表单数据进行Unicode编码

    # 构建请求对象
    req = request.Request(base_url,data=bytes(form_data,encoding='utf-8'))

    # 发送请求
    response = request.urlopen(req)

    data = response.read()

    data = json.loads(data)
    for i in data['data']:
        print('\t'+i['v'])


if  __name__=="__main__":
    print('输入"q"退出程序')
    while True:
        kw = input('请输入：')
        if kw == 'q':
            break
        else:
            fanyi(kw)




