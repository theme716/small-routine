import threading
import time

a = []
def foo(a,i):
    time.sleep(1)
    a.append(i)
    print(i)

for i in range(10):
    t = threading.Thread(target=foo,args=(a,i))
    t.start()

time.sleep(2)
print(a)