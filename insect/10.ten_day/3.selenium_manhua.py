from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time,requests,re,os
from lxml import etree
from urllib.parse import urljoin

class manHua:
    def __init__(self):
        self.chile_url = 'http://www.omanhua.com/comic/4239/'
        self.browser = webdriver.Chrome(executable_path=r'E:\software\browser\chromedriver_win32\chromedriver.exe')
        self.wait = WebDriverWait(self.browser, 20)

    def main(self):
        a = 'http://www.omanhua.com/comic/21109/'
        all_link = self.get_all(a)
        for link in all_link:
            self.get_all_page_url(link)

    def get_all(self,url):
        '''
        从漫画主页提取所有话的链接女
        :param url: 漫画主页
        :return:返回一个有所有链接的列表
        '''
        response = self.get_response(url)
        html = response.text
        html = etree.HTML(html)
        all_link = html.xpath('//div[@class="subBookList"]//a/@href')
        all_link = [urljoin('http://www.omanhua.com/comic/21109/386256/',link) for  link in all_link]
        return all_link

    def get_all_page_url(self,url):
        '''
        漫画网页,提取漫画的总页数，然后循环提取图片链接函数，建立哪个漫画第几话的文件夹
        :param url: 漫画网页链接
        :return: 返回一个图片链接
        '''
        response = self.get_response(url)
        html = response.text
        html = etree.HTML(html)
        # 获取总页数
        num_page = html.xpath('//body/div[2]/div[2]/span/text()')[-1]
        num_page = re.search(r'/(.+?)\)',num_page,re.S).group(1)
        # 获取漫画名称
        manhua_name = html.xpath('//h1/a/text()')[0]
        # 获取漫画第几话
        manhua_num = html.xpath('//h2/text()')[0]
        # 新建文件夹
        if not os.path.exists('./manhua/'+manhua_name):
            os.makedirs('./manhua/'+manhua_name)
        dirurl = './manhua/'+manhua_name+'/'+manhua_num
        if not os.path.exists(dirurl):
            os.makedirs(dirurl)

        for i in range(1,int(num_page)+1):
            full_url = url+'index.html?p='+str(i)
            self.get_pic_url(full_url,dirurl)
            print(i)

    def get_pic_url(self,url,dirurl):
        '''
        提取每个网页中的图片链接，分配到下载图片函数
        :param url: 每一页漫画的url  http://www.omanhua.com/comic/21109/386255/index.html?p=1
        :param dirurl: 存储图片的路径
        '''
        dir_url = dirurl
        self.browser.get(url)
        self.wait.until(expected_conditions.presence_of_all_elements_located((By.ID,'mangaFile')))
        html = self.browser.page_source
        html = etree.HTML(html)
        # 提取图片url
        pic_url = html.xpath('//img[@id="mangaFile"]/@src')[0]
        self.down_pic(pic_url,dir_url)
        print(pic_url)

    def down_pic(self,url,dir_url):
        '''
        下载图片的方法
        :param url:图片链接
        :param dir_url: 存储图片的路径
        '''
        pic_url = dir_url+url[url.rfind('/'):]
        response = requests.get(url)
        pic_text = response.content
        with open(pic_url,'wb') as f:
            f.write(pic_text)

    def get_response(self,url):
        '''
        发送请求的方法
        :param url: 发送请求的路径
        :return: 返回一个response对象
        '''
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        return response

    def __del__(self): #退出时关闭浏览器
        self.browser.close()

if __name__ == '__main__':
    manhua = manHua()

    # 下载某一话的所有漫画的试验
    # manhua.get_all_page_url('http://www.omanhua.com/comic/21109/386255/')
    # 从某一个漫画主页提取所有分页的试验
    manhua.main()

