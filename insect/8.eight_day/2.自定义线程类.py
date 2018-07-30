from threading import Thread

class MyThread(Thread):
    def __init__(self,num):
        # Thread.__init__(self)
        super(MyThread, self).__init__()
        self.num = num
    # 调用start方法就被调用
    def run(self):
        print('{}线程启动'.format(self.num))

t = MyThread(1)
t.start()

