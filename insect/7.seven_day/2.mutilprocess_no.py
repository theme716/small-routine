import multiprocessing
import os
import requests

# 子进程任务函数
def child(url):
    response = requests.get(url)
    print(response.status_code)
    print(os.getpid())
    print(os.getppid())
    print('==============')

if __name__ == '__main__':

    base_url = 'https://hr.tencent.com/position.php?start=%d'
    for i in range(0,90+1,10):
        fullurl = base_url%i

        # 实例化一个子进程对象
        # tartget:子进程的任务函数
        p = multiprocessing.Process(target=child,args=(fullurl,))
        # 启动子进程
        p.start()
        
        
# 这种做法是错误的，因为有多少个任务就会有多少个进程，而进程不能无限制增多
# 所以需要将任务放到一个队列里面，用固定的进程数执行队列里面的任务,这也资源共享的方法