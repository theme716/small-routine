import threading
from queue import Queue
import requests
from bs4 import BeautifulSoup

concurrent = 3 # 并发采集数
conparse = 3 # 并发解析数

# 采集数据线程类
class Crawl(threading.Thread):
    def __init__(self,i,task_q,data_q):
        self.i = i
        self.task_q = task_q
        self.data_q = data_q
        super(Crawl, self).__init__()


    def run(self):
        print('%d采集启动了' % self.i)
        while not self.task_q.empty():
            url = self.task_q.get()
            print(url)
            response = requests.get(url)
            response.encoding = 'utf-8'
            html = response.text
            self.data_q.put(html)
        print('%d采集结束了' % self.i)


# 解析数据线程类
class Parse(threading.Thread):
    def __init__(self,i,t_list,data_q,lock):
        self.i = i
        self.data_q = data_q
        self.t_list = t_list
        self.is_parse = True  # 是否进行数据解析
        self.lock = lock
        super(Parse, self).__init__()

    def run(self):
        print('%d解析启动了' % self.i)
        while True:
            # 判断采集进程运行状态
            for t in self.t_list: #遍历数据采集对象列表
                if t.is_alive(): # 三个线程都在进行中，就break,如果有空闲的，进入else
                    break

            else:
                if self.data_q.empty():
                    self.is_parse = False


            if self.is_parse:  #if则可以进行数据解析
                # 从数据队列提取数据解析
                try:
                    html = self.data_q.get(timeout=3)
                    self.parse(html)
                except:
                    pass
            else:
                break

        print('%d解析结束了' % self.i)

    def parse(self,html):
        html = BeautifulSoup(html,'lxml')
        print(html.title.text)


def main():
    lock = threading.Lock()
    task_q = Queue() #任务队列（里面是一串的url）
    data_q = Queue() #网页队列（里面是一串的html）
    # 创建任务
    base_url = 'https://www.qiushibaike.com/8hr/page/%d/'
    for i in range(1,14):
        fullurl = base_url % i
        task_q.put(fullurl)
        # response = requests.get(fullurl)
        # print(response.status_code)

    # 创建采集线程
    t_list = []
    for i in range(concurrent):
        t = Crawl(i,task_q,data_q)
        t.start()
        t_list.append(t)

    # 创建解析线程
    p_list = []
    for i in range(conparse):
        t = Parse(i,t_list,data_q,lock)
        t.start()
        p_list.append(t)

    for t in t_list:
        t.join()
    for t in p_list:
        t.join()

    print('任务结束')


if __name__ == '__main__':
    main()