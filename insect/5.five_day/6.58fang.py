import requests,os,json,time,random
from urllib import request
from lxml import etree


base_url = 'http://bj.58.com/chuzu/?PGTID=0d200001-0000-1b16-dad8-57171a5a96ef&ClickID={}'

class RepFang:

    def __init__(self):
        # self.proxy = {
        #     'http': 'http://HDYR1721P39U11UD:2477537210F17B7F@http-dyn.abuyun.com:9020',
        #     'https': 'http://HDYR1721P39U11UD:2477537210F17B7F@http-dyn.abuyun.com:9020'
        # }
        if not os.path.exists('./58pics'):
            os.makedirs('58pics')
        self.base_url = 'http://bj.58.com/chuzu/?PGTID=0d200001-0000-1b16-dad8-57171a5a96ef&ClickID={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Cookie': '58home=bj; id58=c5/njVsiUxILq38KA4JWAg==; city=bj; 58tj_uuid=24aa4457-90c4-4518-abad-3864f1e9bedd; als=0; wmda_uuid=6f94d4443458db38ae03654891765933; wmda_new_uuid=1; wmda_visited_projects=%3B2385390625025; commontopbar_myfeet_tooltip=end; xxzl_deviceid=%2FvqwUs9WBktis%2Fnpa8LZlA1P%2BZNTSr7nHxiiKnFPA49euesjsSxoPxgId76sxA%2BP; defraudName=defraud; myfeet_tooltip=end; duibiId=; new_uv=3; utm_source=; spm=; init_refer=; wmda_session_id_2385390625025=1528992649523-ace19af4-cb0f-772d; new_session=0; ppStore_fingerprint=CDE8FF48D2AF178F2A972C37105BBCE7903E4CA5B9C6BA16%EF%BC%BF1528993243545'
        }
        self.zufang_dict_var = {}
        self.hezu_dict_var = {}
        self.pingpaigongyu_dict_var = {}
        self.f = open('./json/58.json', 'w', encoding='utf-8')

    def father_rep(self):
        start = int(input('请输入起始页：'))
        end = int(input('请输入结束页：'))


        for i in range(start,end+1):

            try:
                full_url = self.base_url.format(i)
                # response = requests.get(full_url,headers=self.headers,proxies=self.proxy)
                response = requests.get(full_url,headers=self.headers)
                response.encoding = response.apparent_encoding
                html = response.text
                html = etree.HTML(html)
                all_url = html.xpath('//ul[@class="listUl"]/li//a[1]/@href')
                all_url = all_url[0:-1] #切掉最后一个跳转的链接
                set_var = set() #每个页面的链接删选之后放到这里
                for x in all_url:
                    if 'http:' in x:
                        if '^desc'in x:
                            x = x[:-6]
                            set_var.add(x)
                        else:
                            set_var.add(x)
                return set_var
            except Exception as e:
                print('*********************************')
                print(e)
                print(full_url)
                print('*********************************')

    def child_rep(self):
        '''
        思路：按照房子类型的不同，数据存储至三个json文件，图片存储在一个文件夹
        :return:
        '''
        list_var = self.father_rep()
        for url in list_var:
            # 发送请求部分
            # response = requests.get(url,headers=self.headers,proxies=self.proxy)
            response = requests.get(url,headers=self.headers)
            response.encoding = response.apparent_encoding
            child_url = response.url
            print(child_url)
            print('============')
            if 'http://callback.58.com/firewall/verifycode' in child_url:
                continue
            # 爬取页面
            # 提取链接中的id
            have_wenhao = child_url.find("?") #先把问号后面的参数切掉
            if have_wenhao != -1:
                child_url = child_url[:have_wenhao]

            have_dian = child_url.rfind('.') #把点后面的后缀切掉
            fang_id = child_url[:have_dian]

            have_last_xiegang = fang_id.rfind('/') #获取房子的id
            fang_id = fang_id[have_last_xiegang+1:]

            # 将三种类型的url放到三个请求函数中去
            if 'zufang' in child_url:
                ret = self.zufang_hezu(response,fang_id)
                self.zufang_dict_var[fang_id] = ret
            elif 'hezu' in child_url:
                ret = self.zufang_hezu(response,fang_id)
                self.hezu_dict_var[fang_id] = ret
            elif 'pingpaigongyu' in child_url:
                self.pingpaigongyu(response,fang_id)

    # 合租和租房的数据处理
    def zufang_hezu(self,response,fang_id):
        '''
        这是租房的
        :param response:
        :param fang_id:
        :return:
        '''

        # 这是存储某一个页面数据的字典
        dict_var = {}

        # 接受response对象
        html = response.text
        html = etree.HTML(html)


        # 题目，价格，租房条件的匹配与保存
        title = html.xpath('//h1/text()')
        price = html.xpath('//div[@class="house-pay-way f16"]//b/text()')
        condition = html.xpath('//div[@class="house-pay-way f16"]/span[2]/text()')
        dict_var['price'] = price
        dict_var['title'] = title
        dict_var['condition'] = condition

        # 图片右侧详细信息的保存
        li_list = html.xpath('//div[@class="house-desc-item fl c_333"]/ul/li')
        a = len(li_list)
        # print(title, price, condition, a)  #输出的内容依次为，标题，价格，押一付一，li长度
        for i in range(1,a+1):
            every_name = html.xpath('//div[@class="house-desc-item fl c_333"]/ul/li['+str(i)+']/span[1]//text()')[0] #获取每一个li的第一个span,内容即为字段的标题
            every_content = html.xpath('//div[@class="house-desc-item fl c_333"]/ul/li['+str(i)+']//text()')
            every_content = ''.join(every_content)
            # every_name 里面去掉空格和冒号
            every_name = every_name[:-1]
            # every_content里面去掉空格和换行，再去掉前面的标题（5个字符）
            every_content = ''.join(every_content.split())[5:]
            dict_var[every_name] = every_content
            # print(every_name)
            # print(every_content)


        # 获取下方的房屋信息
        virtue = html.xpath('//ul[@class="introduce-item"]/li[1]/span[2]//text()')
        virtue = ''.join(virtue)
        virtue = ''.join(virtue.split())
        info = html.xpath('//ul[@class="introduce-item"]/li[2]/span[2]//text()')
        info = ''.join(info)
        info = ''.join(info.split())
        dict_var['virtue'] = virtue
        dict_var['info'] = info

        # 获取并下载图片
        pic_list = html.xpath('//ul[@id="housePicList"]//img/@lazy_src')
        print(pic_list)
        # 建立一个文件夹，文件夹名字是id，并保存图片
        dirname = os.path.join('./58pics',fang_id)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        pics = '' # 图片字段
        for picnum in range(0,len(pic_list)):
            # 图片url的处理
            pic_url = pic_list[picnum]
            s = pic_url.rfind('?')
            pic_url = pic_url[:s]
            request.urlretrieve(pic_url,dirname+'/'+str(picnum)+'.jpg') #保存图片
            pics += str(picnum)+'.jpg'+',' #将图片名称加入图片字典的字符创中
        dict_var['pics'] = pics
        time.sleep(random.random()) #休息一下
        return dict_var #返回存有数据的字典

    # 品牌公寓处理
    def pingpaigongyu(self,response,fang_id):
        '''
        这是品牌公寓的请求
        :param response:
        :param fang_id:
        :return:
        '''
        pass

    # 程序结束的时候写入
    def __del__(self):
        self.f.write(json.dumps(self.zufang_dict_var,ensure_ascii=False))
        self.f.write(json.dumps(self.hezu_dict_var,ensure_ascii=False))
        self.f.write(json.dumps(self.pingpaigongyu_dict_var,ensure_ascii=False))
        self.f.close()


if __name__ == '__main__':
    repfang = RepFang()
    repfang.child_rep()

