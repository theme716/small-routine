from gevent import monkey
monkey.patch_all()
import gevent
import requests
from queue import Queue
import time


base_url = 'https://hr.tencent.com/position.php?start=%d'

def get_page(url_q):
    while not url_q.empty():
        url = url_q.get()
        response = requests.get(url,headers={'User-Agent':'nihaotengxun'})
        print(response.status_code,response.url)


start_time = time.ctime()

# 创建任务队列
url_q = Queue()
for i in range(0,3800+1,10):
    full_url = base_url%i
    url_q.put(full_url)

# 创建协程
g_list = []
for i in range(50):
    g = gevent.spawn(get_page,url_q)
    g_list.append(g)

# 开启协程
gevent.joinall(g_list)

print('任务结束')
print(start_time)
print(time.ctime())
