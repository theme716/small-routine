import os
import time

a = 1
newpid = os.fork()

# fork()返回两次
# 给子进程返回0
# 给父进程返回子进程的pid


if newpid == 0:
    print('我是子进程')
    print('我的进程id是:%d'%os.getpid())
    print('我的父进程id是:%d'%os.getppid())

else:

    print('我是父进程,我的进程id是:%d'%os.getpid())



