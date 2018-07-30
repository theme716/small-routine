import scrapy,re
from ..items import AnjukeItem
class Anjuke(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://bj.zu.anjuke.com/fangyuan/p1/']
    base_url = 'https://bj.zu.anjuke.com/fangyuan/p{}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',

        'Cookie': 'aQQ_ajkguid=E5804A7B-9439-83D4-CAA1-6898CB44B2B1; _ga=GA1.2.1739756333.1516272304; 58tj_uuid=30ebb3ca-f2e6-41b4-a158-6ef974e9852b; als=0; lps=http%3A%2F%2Fbj.zu.anjuke.com%2Ffangyuan%2F%7C; ctid=14; twe=2; sessid=130CAAEB-55B6-6A16-BC45-CDD0644150C2; init_refer=; new_uv=16; propertys=jctlsv-pav7t4_; new_session=0; _gid=GA1.2.1816218528.1529907617; _gat=1; __xsptplusUT_8=1; __xsptplus8=8.17.1529906990.1529907634.12%232%7Cwww.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23Z7IGdUA9c4wwG_iy5ksPflddHH1VmzXd%23'
    }
    def parse(self, response):
        for i in range(1,0,-1):
            full_url = self.base_url.format(i)
            yield scrapy.Request(full_url,headers=self.headers,callback=self.get_parse)

    # 列表页提取信息
    def get_parse(self,response):
        div_list = response.css('div.zu-itemmod')
        for div in div_list:
            item = AnjukeItem()

            h_name = div.xpath('.//h3/a/text()').extract()[0]
            info = div.css('p.tag::text').extract()
            h_num = info[0].strip() # 房屋居室
            h_area = info[1].strip() # 房屋面积
            h_level = info[2].strip() # 房屋楼层
            h_agent = info[3].strip() # 房屋经纪人
            h_address = ''.join(div.xpath('.//address/text()').extract()).strip()
            h_price = div.css('strong::text').extract()[0]
            info2 = div.css('p.bot-tag span::text').extract()
            h_info2 = '-'.join(info2)
            h_url = div.css('a.img::attr(href)').extract()[0]

            item['h_name'] = h_name
            item['h_num'] = h_num
            item['h_area'] = h_area
            item['h_level'] = h_level
            item['h_agent'] = h_agent
            item['h_address'] = h_address
            item['h_price'] = h_price
            item['h_info2'] = h_info2
            item['h_url'] = h_url

            yield scrapy.Request(h_url,headers=self.headers,callback=self.get_child_parse,meta={'item':item})

    # 详情页提取信息
    def get_child_parse(self,response):
        agent_phone = re.search("brokerPhone:'(.+?)'",response.text).group(1)
        h_introduce = response.xpath('//div[@class="auto-general"]').extract()[0] # 房间介绍信息

        h_img_room = response.xpath('//div[@id="room_pic_wrap"]//img/@data-src').extract() #室内图片链接列表
        h_img_hx = response.xpath('//div[@id="hx_pic_wrap"]//img/@data-src').extract() #户型图链接列表
        h_img_environment = response.xpath('//div[@id="surround_pic_wrap"]//img/@data-src').extract() #环境图链接列表

        # 寻找房屋编码
        h_id = response.url[response.url.rfind('/')+1:response.url.find('?')]

        item = response.meta['item']

        item['agent_phone'] = agent_phone
        item['h_introduce'] = h_introduce
        item['h_img_room'] = h_img_room
        item['h_img_hx'] = h_img_hx
        item['h_img_environment'] = h_img_environment
        item['h_id'] = h_id
        yield item
