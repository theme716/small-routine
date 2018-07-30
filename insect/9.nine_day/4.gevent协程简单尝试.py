import gevent
import time

# 协程任务
def foo(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(0) #通过gevent.sleep(0)交出控制权，让协程交替进行，要不要会顺序运行
        '''
        # 这才是真正的协程，三个协程同时执行
        <Greenlet "Greenlet-0" at 0x25aea331648: foo(3)> 0
        <Greenlet "Greenlet-1" at 0x25aea331948: foo(3)> 0
        <Greenlet "Greenlet-2" at 0x25aea331a48: foo(3)> 0
        <Greenlet "Greenlet-0" at 0x25aea331648: foo(3)> 1
        <Greenlet "Greenlet-1" at 0x25aea331948: foo(3)> 1
        <Greenlet "Greenlet-2" at 0x25aea331a48: foo(3)> 1
        <Greenlet "Greenlet-0" at 0x25aea331648: foo(3)> 2
        <Greenlet "Greenlet-1" at 0x25aea331948: foo(3)> 2
        <Greenlet "Greenlet-2" at 0x25aea331a48: foo(3)> 2
        '''
        # time.sleep(1)
        '''
        这是输出结果，先是执行协程1，执行三次，然后执行协程2，执行三次..。这不是真正的协程
        <Greenlet "Greenlet-0" at 0x22171a61648: foo(3)> 0
        <Greenlet "Greenlet-0" at 0x22171a61648: foo(3)> 1
        <Greenlet "Greenlet-0" at 0x22171a61648: foo(3)> 2
        <Greenlet "Greenlet-1" at 0x22171a61948: foo(3)> 0
        <Greenlet "Greenlet-1" at 0x22171a61948: foo(3)> 1
        <Greenlet "Greenlet-1" at 0x22171a61948: foo(3)> 2
        <Greenlet "Greenlet-2" at 0x22171a61a48: foo(3)> 0
        <Greenlet "Greenlet-2" at 0x22171a61a48: foo(3)> 1
        <Greenlet "Greenlet-2" at 0x22171a61a48: foo(3)> 2
        '''

g1 = gevent.spawn(foo,3) #将任务函数封装入gevent.spawn(),第一个参数是任务函数，第二个参数是给任务参数传递的参数
g2 = gevent.spawn(foo,3)
g3 = gevent.spawn(foo,3)

g1.join()
'''
gevent的介绍：
    当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
'''
