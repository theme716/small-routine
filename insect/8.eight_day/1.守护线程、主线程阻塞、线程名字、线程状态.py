from threading import Thread,current_thread
import time


# 线程函数
def foo(num):
    print(current_thread().name) #打印线程名字
    time.sleep(2)
    print(num)


# 创建两个线程
t1 = Thread(target=foo,args=(1,),name='t1')
t2 = Thread(target=foo,args=(2,),name='t2')

# 设置t1为守护进程（后台执行）(会将执行程序放在后台执行，主进程瞬间完成，如果设置堵塞，则不生效了)
# t1.setDaemon(True)  #守护线程，后台运行的
# t2.setDaemon(False) #用户线程，前台运行的

t1.start()
t2.start()


# 主进程堵塞
t1.join()
t2.join()
print('======================')
# 获取线程运行状态
print(t1.is_alive())
print(t2.is_alive())