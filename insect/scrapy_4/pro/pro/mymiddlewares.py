from fake_useragent import UserAgent
from scrapy.conf import settings
import random,base64,pymysql

# 得到一个随机的useragent的中间件
class RandomUserAgent(object):
    def __init__(self):
        self.ua = UserAgent()

    def process_request(self,request,spider):
        # 在中间件中给request对象添加一个user-agent
        request.headers['User-Agent'] = self.ua.random

# 这是一个测试的中间件
class Middle1(object):
    def process_request(self,request,spider):
        print('经过request--1')
    def process_response(self,request,response,spider):
        print('经过response--1')
        return response
    def process_exception(self,request,exception,spider):
        pass

# 这是一个测试的中间件
class Middle2(object):
    def process_request(self,request,spider):
        print('经过request--2')
    def process_response(self,request,response,spider):
        print('经过response--2')
        return response
    def process_exception(self,request,exception,spider):
        pass


# 使用setting中的代理，免费代理和验证代理随机使用
class RandomProxySettings(object):
    def process_request(self,request,spider):
        # 导入setting中的ip
        '''
            setting中的ip是一个字典，
                {'host':'xxxx.xxxx.xxxx.xxxx:xxxx'}
                {'host':'1111.1111.1111.1111:xxxxx','auth':'alice:123456'}
        '''
        proxy = random.choice(settings['PROXIES'])

        # 随机选择一个，判断有没有密码
        if proxy.get('auth'): #判断有没有auth这个键，如果有，则为验证代理
            print(proxy['host'],proxy['auth'])
            auth = base64.b64encode(bytes(proxy['auth'],encoding='utf-8')) #给认证信息编码
            request.headers['Proxy-Authorization'] = b'Basic ' + auth #设置代理认证信息
        else:
            # 免费代理
            pass
        request.meta['proxy'] = 'http://%s' % proxy['host']


    def process_response(self,request,response,spider):
        print('经过response中间件')
        return response


# 这是一个随机从数据库中获取代理的中间件
class RandomProxyMysql(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', '123456', 'reptile', charset='utf8')
        self.cursor = self.conn.cursor()
    def random_proxy(self): #获得一个随机的proxy的方法
        sql = ''
        self.cursor.execute(sql)
        proxy = self.cursor.fetchone()
        return proxy

    def process_request(self,request,spider):
        proxy = self.random_proxy()
        request.meta['proxy'] = 'http://%s:%s' % (proxy[1],proxy[2])

    def process_response(self,request,response,spider):
        print(response.status)
        return response



