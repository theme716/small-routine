from threading import Thread
from queue import Queue
import requests,time

def get_page(task_q):
    while not task_q.empty():
        url = task_q.get()
        response = requests.get(url,headers={'User-Agent':'tentxunshazi'})
        print(response.url)


if __name__ == '__main__':

    time_start = time.ctime() #程序运行起始时间

    task_q = Queue()
    base_url = 'https://hr.tencent.com/position.php?start=%d'
    # 将任务放入任务队列中
    for i in range(0,3760+1,10):
        full_url = base_url%i
        task_q.put(full_url)

    # 开启线程
    t_list = []
    for i in range(50):
        t = Thread(target=get_page,args=(task_q,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print('程序开始时间：')
    print(time_start)
    print('程序结束时间：')
    print(time.ctime())