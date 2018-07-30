import time

def A():
    while True:
        print('----------------a-------------')
        yield
        time.sleep(1)

def B(a):
    while True:
        print('-----------------b--------------')
        next(a)
        time.sleep(1)

if __name__ == '__main__':
    a = A()
    B(a)

'''
过程思考:
    调用B函数，
    print('----b----')、（中间没有间隔）执行一次a(输出---a---)、b中等待1秒
    print('----b----')、执行一次a(a中等待一秒，输出----a----),b中等待1秒
    print('----b----')、执行一次a(a中等待一秒，输出----a----),b中等待1秒

实质：
    调动b函数的过程中也在调用a,两个都在轮询工作
    
'''