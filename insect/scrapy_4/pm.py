import pymysql,requests
from threading import Thread
from threading import Lock
from queue import Queue
from fake_useragent import UserAgent

'''
思路
1、获取数据库中的所有数据，并放入对列池中
2、创建多线程任务
3、验证函数，发送请求，
'''
# 数据库中获取所有的代理，并添加入队列的函数
def get_all_proxy(proxy_queue,conn,cursou):
    sql = 'select * from proxy'
    row = cursou.execute(sql) #写入sql语句
    data = cursou.fetchall() #查询数据，返回值[(),(),()]
    for proxy in data:
        proxy_queue.put(proxy)

# 多线程的执行函数（从队列中获取代理，发送请求，如果失败，删除）
class ProxyManager(Thread):

    def __init__(self,proxy_queue,conn,cursor,lock):
        super(ProxyManager, self).__init__()
        self.proxy_queue = proxy_queue #获得有着各个代理的队列
        self.conn = conn # 获得数据库连接对象
        self.cursor = cursor # 获得游标对象
        self.ua = UserAgent()
        self.lock = lock #获得线程锁
        print('开启了一个线程')

    def run(self):# 调用过滤代理函数
        self.filter_proxy()

    def filter_proxy(self): #过滤代理的函数
        while not self.proxy_queue.empty():
            proxy_tuple = self.proxy_queue.get()
            url = 'http://www.baidu.com'
            proxy = {
                'http':'http://%s:%s'%(proxy_tuple[1],proxy_tuple[2]),
                'https':'http://%s:%s'%(proxy_tuple[1],proxy_tuple[2])
            }
            try:
                response = requests.get(url=url,proxies = proxy,timeout=10,headers={'User-Agent':self.ua.random})
                if 200 <= response.status_code <= 300: #有的代理会给你返回一个407之类的东西
                    print(response.status_code,proxy_tuple,'正常')
                else:
                    with self.lock:
                        self.del_proxy(proxy_tuple)

            except Exception as e:
                # 第二次重试机会，可以再连接一次
                try:
                    response = requests.get(url=url, proxies=proxy,timeout=10, headers={'User-Agent': self.ua.random})
                    if 200 <= response.status_code <= 300:
                        print(response.status_code, proxy_tuple, '正常')
                    else:
                        with self.lock:
                            self.del_proxy(proxy_tuple)
                # 第二次连接重试失败，删掉
                except Exception as e:
                    # 删掉这个
                    with self.lock:
                        self.del_proxy(proxy_tuple)


    def del_proxy(self,proxy_tuple):
        '''
        删除代理的函数
        '''
        sql = 'delete from proxy where id=%d'%proxy_tuple[0]
        try:
            row = self.cursor.execute(sql)
            self.conn.commit()
            print(proxy_tuple,'被删除了')
        except Exception as e:
            print('=========================删除数据库报错==============')
            print(e)

def main():
    # 创建数据库连接
    conn = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
    cursor = conn.cursor()

    # 创建队列，并将数据库查询到的ip放入队列中
    proxy_queue = Queue()
    get_all_proxy(proxy_queue,conn,cursor)

    lock= Lock()

    # 创建多线程
    t_list = []
    for i in range(150):
        t = ProxyManager(proxy_queue,conn,cursor,lock)
        t.start()
        t_list.append(t)

    t_list = [t.join() for t in t_list]

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()


'''
要点：
1、删除代理的时候，要用线程锁锁住，因为这个时候要使用同一个数据库连接对象和游标对象，可能出现报错
2、数据库操作时候很容易报错，加一个try比较好。
'''