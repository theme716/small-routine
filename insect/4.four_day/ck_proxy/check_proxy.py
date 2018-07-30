from urllib import request
import re,json

def proxy_dict(proxy):
    '''
    :param proxy:传入一个ip字典
    :return: 返回一个合适的proxy字典
    '''
    proxy = {
        'http':'http://'+proxy['ip']+':'+proxy['端口号'],
        'https':'http://'+proxy['ip']+':'+proxy['端口号']
    }
    return proxy


base_url = 'http://www.baidu.com/s?wd=ip'
with open('xici.json','r',encoding='utf-8') as f:
    proxy_list = f.read()
# 将json格式数据转码
proxy_list = json.loads(proxy_list)
for one_proxy in proxy_list:


    proxy = proxy_dict(one_proxy)
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    # 设置全局默认的opener对象
    request.install_opener(opener)

    try:
        response = request.urlopen(base_url,timeout=5)
        html = response.read().decode()
        ip_pat = re.compile(r'class="c-gap-right">(.+?)</span>')
        res = ip_pat.search(html)
        if res:
            print('1',proxy,'正常使用')
        else:
            print('2',proxy,'不能使用')
    except Exception as e:
        print('3',proxy,e)

