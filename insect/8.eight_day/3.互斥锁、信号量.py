# 互斥锁
'''
from threading import Thread,Lock

num = 0

#创造一个互斥锁
lock = Lock()

# 在编程中，引入了对象互斥锁的概念，来保证共享数据操作的完整性。每个对象都对应于一个可称为" 互斥锁" 的标记，这个标记用来保证在任一时刻，只能有一个线程访问该对象。

def add():
    global num
    for i in range(1000000):

        # 上锁姿势：一
        # lock.acquire() # 上锁
        # num += 1
        # lock.release() # 解锁

        # 上锁姿势：二
        with lock:
            num += 1



t1 = Thread(target=add)
t2 = Thread(target=add)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
'''

# 信号量
'''
from threading import Thread,BoundedSemaphore
import time

def foo(i):
    bs.acquire() #上锁
    time.sleep(1)
    print(i)
    bs.release() #解锁


bs = BoundedSemaphore(3) #同时执行的线程数

for i in range(10):
    t = Thread(target=foo,args=(i,))
    t.start()
'''