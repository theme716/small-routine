'''
目标：练习使用数据库存储，下载图片，多个管道处理item
'''
import scrapy,re,json
from .. settings import COOKIE
from ..items import BaiheItem

class baihe(scrapy.Spider):
    name = 'baihe'
    allowed_domains = []
    start_urls = ['http://www.baidu.com']

    id_list = 'http://search.baihe.com/Search/getUserID?&jsonCallBack=jQuery18304023144646136796_1530003036835&page={}'
    friend_list_url = 'http://search.baihe.com/search/getUserList?userIDs={}&jsonCallBack=jQuery18304023144646136796_1530003036837'
    friend_url = 'http://profile1.baihe.com/?oppID={}'

    headers = {
        "Connection": "keep-alive",
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://search.baihe.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://search.baihe.com/",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    json_pat = re.compile(r'\{.+\}',re.S)


    def parse(self, response):
        '''
        :param response:没有用的，百度请求的response
        :return: 返回一个获取用户id json的任务
        '''
        print(response.status)
        for i in range(2,0,-1):
            full_url = self.id_list.format(i)
            yield scrapy.Request(url=full_url,callback=self.get_id,headers=self.headers,cookies=COOKIE)

    def get_id(self,response):
        '''
        :param response: 用户id json文件
        :return: 返回值是一个获得用户信息的json文件，内有多个用户信息
        '''
        # 处理json,结果为一个列表
        data = response.text
        data = self.json_pat.search(data).group()
        data = json.loads(data)
        data = data['data'] # 一个有着各种id的列表

        for i in range(0,len(data),8):
            ids = ','.join(data[i:i+8])
            full_url = self.friend_list_url.format(ids)
            print(full_url)
            yield scrapy.Request(url=full_url,callback=self.friend_json,headers=self.headers,cookies=COOKIE)

    def friend_json(self,response):
        data = response.text
        data = self.json_pat.search(data).group()
        # data = data.encode('gbk')
        data = json.loads(data)
        data = data['data']
        for friend in data: # friend是一个一个字典
            item = BaiheItem()
            item['userID'] = friend['userID']
            item['gender']= friend['gender']
            item['nickname'] = friend['nickname']
            item['age'] = friend['age']
            item['height'] = friend['height']
            item['educationChn'] = friend['educationChn']
            item['marriageChn'] = friend['marriageChn']
            item['incomeChn'] = friend['incomeChn']
            item['cityChn'] = friend['cityChn']
            full_url = self.friend_url.format(friend['userID'])
            item['one_url'] = full_url
            yield scrapy.Request(url=full_url,callback=self.friend,headers=self.headers,cookies=COOKIE,meta={'item':item})

    def friend(self,response):
        '''
        :param response: 提取女朋友个人主页信息
        :return:
        '''
        item = response.meta['item']
        pic_list = response.css('div.big_pic ul img::attr(src)').extract() # 照片路径列表
        woman_introduce_tag = ','.join(response.xpath('//div[@class="womanData"]/div[@class="inter label"]//span/text()').extract()) # 自我标签
        perData_intr = response.xpath('//div[@class="perData"]//div[@class="intr"]/text()').extract()[0].strip() #个人介绍
        # print(pic_list,woman_introduce_tag,perData_intr)
        item['pic_list'] = pic_list
        item['woman_introduce_tag'] = woman_introduce_tag
        item['perData_intr'] = perData_intr

        yield item




