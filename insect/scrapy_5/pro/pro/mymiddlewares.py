from fake_useragent import UserAgent
import random
from scrapy.conf import settings
import base64

class RandomUserAgentCookie(object):

    def __init__(self):
        self.ua = UserAgent()
        self.cookie = 'user_trace_token=20171116192426-b45997e2-cac0-11e7-98fd-5254005c3644; LGUID=20171116192426-b4599a6d-cac0-11e7-98fd-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFC0E3267F681504E5726030548F107348; _gat=1; X_HTTP_TOKEN=d8b7e352a862bb108b4fd1b63f7d11a7; _gid=GA1.2.1718159851.1510831466; _ga=GA1.2.106845767.1510831466; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510836765,1510836769,1510837049,1510838482; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510839167; LGSID=20171116204415-da8c7971-cacb-11e7-930c-525400f775ce; LGRID=20171116213247-a2658795-cad2-11e7-9360-525400f775ce'

    def process_request(self,request,spider):
        request.headers['Host'] = 'www.lagou.com'
        # request.headers['Connection'] = 'keep-alive'
        request.headers['Cache-Control'] = 'max-age=0'
        request.headers['Upgrade-Insecure-Requests'] = 1
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

        request.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        request.headers['Accept-Language'] = "zh-CN,zh;q=0.9"
        request.headers['Cookie'] = self.cookie

class RandomProxySettings(object):
    def process_request(self,request,spider):
        proxy = random.choice(settings['PROXIES'])
        if proxy.get('auth'):
            print(proxy['host'],proxy['auth'])
            auth = base64.b64encode(bytes(proxy['auth'],encoding='utf-8')) #给认证信息编码
            request.headers['Proxy-Authorization'] = b'Basic ' + auth #设置代理认证信息
        else:
            pass
        request.meta['proxy'] = 'http://%s' % proxy['host']
