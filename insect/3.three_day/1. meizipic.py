from urllib import request
import random,time,os,re

# base_utl = 'http://www.umei.cc/p/gaoqing/cn/'
class MeiziPic:
    '''
    在调用分类链接的时候，建立分类链接的文件夹
    '''

    def __init__(self):
        if not os.path.exists('./meizi_pic/'):
            os.makedirs('./meizi_pic')

    def father_urls(self,father_url,start=None,end=None):
        '''
        参数：
            1、分类网页链接
            2、开始页码数
            3、结束页码数
        '''
        # 获取总的页数
        req = request.Request(father_url, headers=self.create_headers())
        response = request.urlopen(req)
        html = response.read().decode()
        father_pat = re.compile(r'<li><a href=.+?index-(\d+?)\.htm.+?>末页')
        father_total_page = father_pat.search(html)
        if not father_total_page:
            a = father_url.rfind('/')
            b = father_url.rfind('.')
            father_total_page = father_url[a+1:b]
        else:
            father_total_page = father_total_page.group(1)
        if start:
            start = int(start)
            if start <= 0:
                print('你输入的起始页小于1，我们将从第一页开始')
                start = 1
        else:
            start = 1
        if end:
            end = int(end)
            if end > int(father_total_page):
                print('您输入的范围超出最大页码,我们将从最大页码开始')
                end = int(father_total_page)
        else:
            end = int(father_total_page)

        for i in range(start,end+1):

            a = father_url.rfind('/')
            b = father_url.rfind('.')
            full_url = father_url[:a]+'/'+str(i)+father_url[b:]
            self.child_urls(full_url)


    def child_urls(self,base_url):
        '''
        参数：分类url
        '''
        req  = request.Request(base_url,headers=self.create_headers())
        response = request.urlopen(req)
        html = response.read().decode()

        child_pat = re.compile(r'li>\s+<a href="(.+?)" class="TypeBigPics" target="_blank"><img.+?class="ListTit">(.+?)</div>',re.S)
        child_group = child_pat.findall(html)
        for child_url,child_name in child_group:
            self.last_pic(child_url)


    def last_pic(self,last_url):
        '''
        目的：1. 输入一个链接，可以爬取下这张图片来
        参数要求：一个图片网页的链接
        结果：在合适的位置生成一张图片
        '''
        # 处理一下 last_url,将后面的_数字去掉
        if '_' in last_url:
            start = last_url.rfind('_')
            end = last_url.rfind('.')
            last_url = last_url[0:start]+last_url[end:]

        # 先建立合适的文件夹
        # 请求这个页面：获取分类 和 图片链接
        req = request.Request(last_url,headers=self.create_headers())
        response = request.urlopen(req)
        html = response.read().decode()
        # 匹配分类
        last_fenlei_pat = re.compile(r'<div class="l">(.+?)<h1 class="inline">(.+?)</h1>浏览</div>')
        last_fenlei = last_fenlei_pat.findall(html)[0]
        # 这是这组图片的名称
        last_fenlei_name = last_fenlei[1] # 什么什么大胸
        last_fenlei_pat_2 = re.compile(r'<a href=.+?>(.+?)<')
        last_fenlei_2 = last_fenlei_pat_2.findall(last_fenlei[0])  #( 主页，国内)
        if not os.path.exists(os.path.join('./meizi_pic/',last_fenlei_2[1])):
            os.makedirs(os.path.join('./meizi_pic/',last_fenlei_2[1]))
            os.makedirs(os.path.join('./meizi_pic/',last_fenlei_2[1],last_fenlei_name))
        else:
            if not os.path.exists(os.path.join('./meizi_pic/',last_fenlei_2[1],last_fenlei_name)):
                os.makedirs(os.path.join('./meizi_pic/', last_fenlei_2[1], last_fenlei_name))
        pic_url = os.path.join('./meizi_pic/', last_fenlei_2[1], last_fenlei_name)

        # 下载组图
        # 先获取总页数
        total_page_pat = re.compile(r'<li><a>共(\d+?)页: </a></li>')
        total_page = total_page_pat.search(html)
        total_page = total_page.group(1)
        # 爬取图片
        for page in range(0, int(total_page)):
            # 将链接处理成每一个图片页面的链接
            full_url = last_url.split('.')
            full_url[-2] = full_url[-2] + '_' + str(page + 1)
            full_url = '.'.join(full_url)
            # 请求
            req = request.Request(full_url, headers=self.create_headers())
            response = request.urlopen(req)
            html = response.read().decode()
            # 正则：
            every_pic_pat = re.compile(r'align="center".+?<img.+?src="(.+?)"',re.S)
            every_pic = every_pic_pat.search(html)
            every_pic_url = every_pic.group(1)
            one_pic_url = os.path.join(pic_url,str(page)+'.jpg')
            # 保存图片
            request.urlretrieve(every_pic_url,one_pic_url)
            print(one_pic_url)

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


if __name__ == '__main__':
    a = MeiziPic()
    # a.last_pic('http://www.umei.cc/p/gaoqing/cn/128401_4.htm')
    # a.child_urls('http://www.umei.cc/p/gaoqing/cn/')
    # a.father_urls('http://www.umei.cc/p/gaoqing/cn/')
    # a.father_urls('http://www.umei.cc/p/gaoqing/rihan/141.htm',1,2)

