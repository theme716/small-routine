import threading
import time

def foo1():
    print('开始执行foo1')
    time.sleep(5) #长延时操作
    print('结束执行foo1')

def foo2():
    print('开始执行foo2')
    time.sleep(3)
    print('结束执行foo2')

# 创建两个子线程
t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

# 启动两个线程
t1.start()
t2.start()

print('END---END')