from queue import Queue
from multiprocessing  import Process,Manager,Queue


def a(q):
    q.put(1)

if __name__ == '__main__':
    # m = Manager()
    # q = m.Queue() #yes
    # q = Queue() # no
    q = Queue()

    # 创建10个进程
    li = []
    for i in range(10):
        t = Process(target=a,args=(q,))
        t.start()
        li.append(t)

    for t in li:
        t.join()

    while not q.empty():
        s = q.get()
        print(s)
