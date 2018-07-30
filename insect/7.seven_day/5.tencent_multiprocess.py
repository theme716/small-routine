import multiprocessing
from multiprocessing import Manager
import time,requests

def task(task_q):
    while not task_q.empty():
        url = task_q.get()
        response = requests.get(url)
        print(response.status_code)

if __name__ == '__main__':
    print(time.ctime())

    # 构建任务队列
    m = Manager()
    task_q = m.Queue()

    # 向任务队列中添加任务
    base_url = 'https://hr.tencent.com/position.php?start=%d'
    for i in range(0,90+1,10):
        fullurl = base_url%i
        task_q.put(fullurl)


    # 创建进程,一共创建15个进程，每一个进程都从队列里领取任务，队列里的任务由进程领取后自动 消亡
    p_list = []
    for i in range(15):
        p = multiprocessing.Process(target=task,args=(task_q,))
        p.start()
        p_list.append(p)

    # 等待主进程
    for p in p_list:
        p.join()

    print(time.ctime())