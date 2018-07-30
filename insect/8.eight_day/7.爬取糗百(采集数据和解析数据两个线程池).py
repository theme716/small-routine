from threading import Thread
from queue import Queue
import requests
from bs4 import BeautifulSoup

concurrent = 3 #并发采集数
conparse = 3 #并发解析数


# 采集数据的类
class Crawl(Thread):
    def __init__(self,i,task_q,data_q):
        super(Crawl, self).__init__()
        self.i = i
        self.task_q = task_q
        self.data_q = data_q

    def run(self):
        '''
        执行数据采集：从任务队列里面取url,然后发起请求，将返回的数据放到data_q队列里面
        每一个t对象，即数据采集对象的task_q队列都指向同一个队列地址，每一个线程都从这个队列里面领取任务，直到任务为空
        :return:
        '''
        print('-----------------------------')
        print('%d采集开始'%self.i)
        while not self.task_q.empty():
            url = self.task_q.get()
            response = requests.get(url)
            response.encoding = 'utf-8'
            html = response.text
            self.data_q.put(html)
            print('%d=-=-=-=-=-=-=%s'%(self.i,url))
        print('%d采集结束'%self.i)
        print('============================--')

# 解析数据的类
class Parse(Thread):
    def __init__(self,i,t_list,data_q):
        Thread.__init__(self)
        self.i = i #这是每一个解析任务进程编号
        self.t_list = t_list #这里面放的是采集数据线程列表
        self.data_q = data_q #这个data_q是不断变化的
        self.is_parse = True #是否进行数据解析

    def run(self):

        print('%d-------解析开始了' % self.i)
        while True:

            for t in self.t_list:
                if t.is_alive():
                    break #本线程已经结束，即已经没有了需要采集的数据
            else: #有正在进行的采集数据线程
                if self.data_q.empty(): #如果解析任务列表为空
                    self.is_parse = False #不进行数据解析
                    
            if self.is_parse: #可以进行数据解析
                try:
                    html = self.data_q.get(timeout=3)
                    self.parse(html)
                except:
                    pass
            else:
                print('test')
                break #终止循环
            '''

            for t in self.t_list:
                if t.is_alive():# 采集线程线程没有完成，还在进行中
                    if self.data_q.empty(): #没有需要解析的数据
                        print('aaaaaa')
                        break #继续便利
                    else: #有需要解析的数据，进行数据解析
                        print('11111')
                        self.parse(self.data_q.get(timeout=3)) #解析数据
                else: #采集数据进程都结束了
                    if self.data_q.empty(): #没有需要解析的数据
                        print('bbbbbb')
                        return '结束循环' #结束总的循环（while）
                    else: #有需要解析的数据
                        print('2222')
                        self.parse(self.data_q.get(timeout=3)) #解析数据

            '''
        print('%d-------解析结束了' % self.i)

    def parse(self,html):
        html = BeautifulSoup(html,'lxml')
        print(html.title.text)


# 主程序
def main():
    task_q = Queue() #任务队列（里面是一串url）
    data_q = Queue() #网页队列（里面是一串html）

    # 创建任务队列
    base_url = 'https://www.qiushibaike.com/8hr/page/%s/'
    for i in range(1,3):
        full_url = base_url%i
        task_q.put(full_url)

    # 采集数据队列
    t_list = []
    for i in range(concurrent):
        t = Crawl(i,task_q,data_q)
        t.start()
        t_list.append(t)
    # 解析数据队列
    p_list = []
    for i in range(conparse):
        p = Parse(i,t_list,data_q)
        p.start()
        p_list.append(p)

    # 采集数据和解析数据的线程是同时的，
    # 需要判断某个任务有没有采集完，只有采集完才可以开始解析
    # 换言之：只有所有的采集线程结束，且data_q里面为空时，才可以终止解析
    for t in t_list:
        t.join()
    for p in p_list:
        p.join()

    print('任务结束')

if __name__ == '__main__':
    main()