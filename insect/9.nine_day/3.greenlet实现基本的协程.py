from greenlet import greenlet
import time
'''
greenlet实现基本的协程
    Greenlet是python的一个C扩展，来源于Stackless python，旨在提供可自行调度的‘微线程’， 即协程。generator实现的协程在yield value时只能将value返回给调用者(caller)。 而在greenlet中，target.switch（value）可以切换到指定的协程（target）， 然后yield value。greenlet用switch来表示协程的切换，从一个协程切换到另一个协程需要显式指定。
　　当创建一个greenlet时，首先初始化一个空的栈， switch到这个栈的时候，会运行在greenlet构造时传入的函数（首先在test1中打印 12）， 如果在这个函数（test1）中switch到其他协程（到了test2 打印34），那么该协程会被挂起，等到切换回来（在test2中切换回来 打印34）。当这个协程对应函数执行完毕，那么这个协程就变成dead状态。
    https://www.cnblogs.com/xybaby/p/6337944.html
'''
def foo1():
    while True:
        print('---------------A----------')
        g2.switch()
        time.sleep(1)

def foo2():
    while True:
        print('------------B--------------')
        g1.switch()
        time.sleep(1)

g1 = greenlet(foo1)
g2 = greenlet(foo2)

g1.switch()

'''
greenlet可以实现协程，不过每一次都要人为的去指向下一个该执行的协程，显得太过麻烦。python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent
'''
