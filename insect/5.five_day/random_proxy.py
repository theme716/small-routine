from urllib import request
import random
import requests

class Proxy():
    def __init__(self,fname):
        with open(fname,'r',encoding='utf-8') as f:
            self.proxy_list = f.readlines()

    def random_proxy(self):
        proxy = random.choice(self.proxy_list)
        proxy_info = proxy.split(',')
        host = proxy_info[0]
        port = proxy_info[1].strip()
        proxy = {
            'http': 'http://%s:%s' % (host, port),
            'https': 'http://%s:%s' % (host, port)
        }
        return proxy

    def dowloader(self,req,headers=None,timeout=10,retry=2):
        '''
        :param req: 请求对象，如果使用requestsbao,则是url
        :param headers:
        :param timeout:
        :param retry:
        :return:
        '''
        if not headers:
            headers = {}
        try:
            proxy = self.random_proxy()
            print(proxy)
            response = requests.get(req,headers=headers,timeout=timeout,proxies=proxy)
            response.encoding = response.apparent_encoding
            return response
        except Exception as e:
            print(e)
            if retry > 0:
                self.dowloader(req,headers=headers,timeout=timeout,retry=retry-1)

if __name__ == '__main__':
    p = Proxy('66.csv')
    base_url = 'http://www.baidu.com'
    response = p.dowloader(base_url,timeout=5)