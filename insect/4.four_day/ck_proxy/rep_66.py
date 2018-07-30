from urllib import request,parse
import re,random,json,os,time

class RepSix:

    base_url = 'http://www.66ip.cn/{}.html'

    def __init__(self):
        '''
        输入起始页和结束页的函数
        '''
        self.start = int(input('请输入起始页:'))
        self.end = int(input('请输入结束页:'))
        self.max_page = int(self.decide_maxpage())
        if self.max_page < self.end:
            print('输入的页码超出最大页码数：')
            print('我们将爬取最多页内容')
            self.end = self.max_page

    def rep(self):
        '''
        :return:没有返回值，直接生成json文件
        '''
        if os.path.exists('66ip.json'):
            os.remove('66ip.json')
        f = open('66ip.json','a',encoding='utf-8')
        f.write('[\n')
        for i in range(self.start,self.end+1):
            time.sleep(random.random()*0.5)
            full_url = self.base_url.format(i)
            req = request.Request(full_url,headers=self.create_headers())
            response = request.urlopen(req)
            html= response.read().decode('gbk')
            ip_pat = re.compile(r'<tr><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td>',re.S)
            ip_data = ip_pat.findall(html)
            # 将数据重组成json格式
            for x in range(0,len(ip_data[1:])):
                dict_var = dict(zip(('ip','端口号','代理位置','代理类型','验证时间'),ip_data[1:][x]))
                # 将每个字典后面加逗号和换行符，如果是最后一个字典，则不添加逗号
                if i == self.end and x == (len(ip_data[1:])-1):
                    f.write(json.dumps(dict_var,ensure_ascii=False)+'\n')
                else:
                    f.write(json.dumps(dict_var,ensure_ascii=False)+',\n')
        f.write(']')
        f.close()


    def create_headers(self):
        '''
        :return:返回请求头
        '''
        useragent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        ]
        self.headers = {
            'User-Agent':random.choice(useragent_list)
        }
        return self.headers



    def decide_maxpage(self):
        '''
        :return:返回66ip最大页码数
        '''
        req = request.Request(self.base_url.format(1),headers=self.create_headers())
        response = request.urlopen(req)

        data = response.read().decode('gbk')
        maxpage_pat = re.compile(r'class="dotdot".+?html">(.+?)</a>',re.S)
        maxpage = maxpage_pat.search(data)
        return maxpage.group(1)

if __name__ == '__main__':
    aa = RepSix()
    aa.rep()

