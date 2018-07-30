import os
import time

def child():

    print('我是子进程')
    print('我的id是:%d,父进程id是:%d'%(os.getpid(),os.getppid()))
    time.sleep(10)
    # 每一个子进程,都复制了所有的代码,即子进程也会生成新的子进程,如果这样,那么这个循环会变为死循环,所以需要用os终端子进程
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()

        else:
            print('我是父进程')
            print('我的id是:%d-----子进程id是:%d'%(os.getpid(),newpid))

        print('text=============')
        if input() == 'q':
            break
parent()
