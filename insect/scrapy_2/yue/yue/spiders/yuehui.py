'''
目标：爬取网易同城约会网站，练习使用多个item，数据库一对多
'''
import scrapy,json,math
from ..items import YueHuiItem,HeartItem


class yuehui(scrapy.Spider):
    name = 'yuehui'
    allwoed_domains = ['163.com']
    start_urls = ['http://yuehui.163.com/searchusersrcm.do?ajax=1&ageBegin=18&ageEnd=40&aim=-1&marriage=0&mode=4&order=8&province=19&city=0&district=-1&sex=0&userTag=0&vippage=-1&searchType=0&page=1&pagesize=81']
    friend_json = 'http://yuehui.163.com/searchusersrcm.do?ajax=1&ageBegin=18&ageEnd=40&aim=-1&marriage=0&mode=4&order=8&province=19&city=0&district=-1&sex=0&userTag=0&vippage=-1&searchType=0&page={}&pagesize=81'
    friend_url = 'http://yuehui.163.com/viewuser.do?id={}'
    heart = 'http://yuehui.163.com/getqalist.do?ajax=1&type=-1&id={}&page={}&pagesize={}'

    def parse(self, response):
        '''
        :param response:
        :return: 随便发送一个请求，获取一共有多少个json页，从而构建分发请求
        '''
        data = response.text
        data = json.loads(data)
        total = data[0]['total']
        max_page = math.ceil(total / 81)
        # for i in range(max_page,0,-1):
        for i in range(2, 0, -1):
            full_url = self.friend_json.format(i)
            yield scrapy.Request(full_url,callback=self.parse_list)

    def parse_list(self,response):
        data = response.text
        data = json.loads(data)
        data = data[0]['list']
        for friend in data:
            item = YueHuiItem()
            item['status'] = '0'
            age = friend['age'] # 年龄
            cityName = friend['cityName'] #城市
            degreeName = friend['degreeName'] # 学历
            districtName = friend['districtName'] #地区
            uid = friend['id'] # 用户id
            incomeName = friend['incomeName'] # 收入
            industryName = friend['industryName'] # 职业
            marriageName = friend['marriageName'] # 婚否
            nick = friend['nick'] #昵称
            full_url = self.friend_url.format(uid)

            item['age'] = age
            item['cityName'] = cityName
            item['degreeName'] = degreeName
            item['districtName'] = districtName
            item['uid'] = uid
            item['incomeName'] = incomeName
            item['industryName'] = industryName
            item['marriageName'] = marriageName
            item['nick'] = nick
            item['full_url'] = full_url


            yield scrapy.Request(url=full_url,callback=self.friend,meta={'item':item})

    def friend(self,response):

        item = response.meta['item']
        pic_list = response.xpath('//div[@class="imagewrap"]//img/@src').extract()
        # 过滤掉这些 /images/blank.gif', '/images/blank.gif', '/images/blank.gif', '/images/blank.gif',
        pic_list = ','.join(pic_list)
        pic_list = pic_list.replace(',/images/blank.gif','')
        pic_list = pic_list.split(',')

        introduction = '。'.join(response.xpath('//div[@class="ctwrap"]/p/text()').extract())
        item['pic_list'] = pic_list
        item['introduction'] = introduction
        print(item['full_url'])
        yield item
        
        # 发送真心话的第一次试探请求
        full_urll = self.heart.format(item['uid'],1,1)

        yield scrapy.Request(url=full_urll,callback=self.heart_total,meta={'uid':item['uid']}) #试探发送一次真心话，看看有没有


    def heart_total(self,response):
        '''
        :param response:
        :return: 发送真心话总请求的一个过度函数
        '''
        uid = response.meta['uid']
        data = response.text
        total = json.loads(data)[0]['total']
        print(total)
        if not total == '0':
            full_url = self.heart.format(uid,1,total)
            yield scrapy.Request(url=full_url,callback=self.heart_parse,meta={'uid':uid})
        else:
            print(str(uid),'没有真心话')

    def heart_parse(self,response):
        uid = response.meta['uid']
        data = response.text
        data = json.loads(data)[0]['list']
        for heart in data:
            item = HeartItem()
            item['status'] = '1'
            item['answer'] = heart['answer']
            item['qid']  = heart['qid']
            item['answered'] = heart['answered']
            item['question'] = heart['question']
            item['typeName'] = heart['typeName']
            item['uid'] = uid
            yield item