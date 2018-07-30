from gevent import monkey
monkey.patch_all() #打一个猴子补丁

# 默认中requests是非延时的请求，而只有延时的io才会激发协程，自动切换任务，
# 打猴子补丁的作用是，将所有的任务都设置为延时操作
import gevent
import requests

# 任务函数
def foo1():
    url = 'http://www.baidu.com'
    response = requests.get(url)
    print(response.url)

def foo2():
    url = 'http://www.google.com'
    try:
        response = requests.get(url,timeout=3)
        print(response.url)
    except:
        pass

def foo3():
    url = 'http://www.taobao.com'
    response = requests.get(url)
    print(response.url)

# 创建协程任务
g1 = gevent.spawn(foo1)
g2 = gevent.spawn(foo2)
g3 = gevent.spawn(foo3)

# 开启协程
gevent.joinall([g1,g2,g3])

print('任务结束')