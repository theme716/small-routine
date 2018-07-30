from queue import Queue
from threading import Thread
import time

class ThreadPool():
    def __init__(self,max_num):
        self.thread_q = Queue(max_num)
        for i in range(max_num):
            self.thread_q.put(Thread)

    def get_thread(self):
        return self.thread_q.get()
    def put_thread(self):
        return self.thread_q.put(Thread)

def foo(i):
    print('{}启动了'.format(i))
    time.sleep(1)
    pool.put_thread() #每使用一个线程池中的线程，都要向池中补充一个线程

if __name__ == '__main__':
    pool = ThreadPool(3) #实例化线程池

    for i in range(10): #生成线程，并放入线程池
        my_thread = pool.get_thread()
        t = my_thread(target=foo,args=(i,))
        t.start()
