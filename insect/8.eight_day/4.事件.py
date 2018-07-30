import threading

def bar(i):
    print('开始执行线程%d' % i)
    event.wait() # 设置阻塞
    print('结束线程执行%d' % i)


event = threading.Event()

for i in range(10):
    t = threading.Thread(target=bar,args=(i,))
    t.start()

res = input()
if res == 'green':
    event.set()

# 当输入green时候，event设置为set(),阻塞放行