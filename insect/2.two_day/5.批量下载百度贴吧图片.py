from urllib import request,parse
import re,random,time,os

class TiebaPic:

    def __init__(self):
        self.url_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        ]
    # 找到自定义的页面
    def page(self):
        '''
        :return:返回一个列表，里面是各个页面的除了host之外的域名
        '''
        urls = []
        tieba_name = input('请输入要爬取的贴吧名字：')
        self.dirname = tieba_name
        start = int(input('请输入要爬取的起始页：'))
        end = int(input('请输入要爬取的结束页：'))
        tieba_name = {
            'kw': tieba_name
        }
        tieba_url = 'https://tieba.baidu.com/f?{tieba}&ie=utf-8&pn='.format(tieba=parse.urlencode(tieba_name))
        for i in range(start, end + 1):
            time.sleep(random.random() * 0.5)
            full_url = tieba_url + str((i - 1) * 50)
            # 构建请求头
            headers = {
                'User-Agent': random.choice(self.url_list)
            }
            # 构建请求对象
            req = request.Request(full_url, headers=headers)
            try:
                # 发送请求
                response = request.urlopen(req)
                html = response.read().decode()
                # 进行正则分析，返回要每一页要爬取的链接：
                div_pat = re.compile(r'class="threadlist_title.+?href="(.+?)".+?</div>', re.S)
                res = div_pat.findall(html)
                # 返回一个个网址
                # ['/p/5729828152', '/p/5737446489', '/p/5742198612', '/p/5742205315', '/p/5739815744', '/p/5736622765',
                #  '/p/5731240610', '/p/5733743102', '/p/5734376677']
                urls += res
            except Exception as err:
                print(err)

        for i in range(0,len(urls)):
            urls[i] = 'https://tieba.baidu.com'+urls[i]
        return urls

    # 找到每一页里面的链接
    def child_page(self,urls):
        time.sleep(random.random()*1)
        urls = urls
        # urls = ['https://tieba.baidu.com/p/5739553352']
        for i in range(0,len(urls)):
            print('=======================第'+str(i+1)+'帖========================')
            print(urls[i])

            try:
                headers = {
                    'User-Agent': random.choice(self.url_list)
                }
                req = request.Request(urls[i],headers=headers)
                response = request.urlopen(req)
                html = response.read().decode()
                # 进行正则分析，返回要每一页要爬取的链接：
                div_pat = re.compile(r'<img class="BDE_Image".+?src="(.+?)".+?>', re.S)
                ree = div_pat.findall(html)
                if ree:
                    if not os.path.exists('./imgs/' + self.dirname + '/'):
                        os.makedirs('./imgs/' + self.dirname)
                    for x in range(0, len(ree)):
                        filename = './imgs/' + self.dirname + '/' + str(i) + '_' + str(x) + '.' + ree[x].split('.')[-1]
                        a = request.urlopen(ree[x])
                        b = a.read()
                        with open(filename,'wb') as f:
                            f.write(b)
                        print(ree[x])
            except Exception as err:
                print(err)

    # 主程序
    def main(self):
        a = self.page()
        print('·································')
        print(a)
        self.child_page(a)



if __name__=='__main__':
    a = TiebaPic()
    a.main()