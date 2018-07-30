import multiprocessing,time
from multiprocessing import Manager


def foo(a,i):
    # a.append(i) #如果a = m.list(),使用列表的方法添加
    # a[i] = i #如果a = m.dict()，使用字典的方法
    a.put(i) #如果a = m.Queue()，这个时候a是一个队列，使用a.put(i)方法添加，使用a.get()方法取出
    print(i)
    time.sleep(1)

if __name__ == '__main__':
    m = Manager()
    # a = m.list()
    a = m.dict()
    # a = m.Queue()

    p_list = [] #进程列表
    for i in range(10):
        p = multiprocessing.Process(target=foo,args=(a,i))
        p.start()
        p_list.append(p)
        # join()方法，在进程执行结束之后执行
        # p.join()

    for p in p_list:
        p.join()

    # 当队列a不为空时，从队列a里面取元素
    while not a.empty():
        num = a.get()
        print(num)

    print('执行完毕')
