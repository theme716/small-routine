import os,requests,time
from urllib import request


def child(url):
    response = requests.get(url)
    print(response.status_code)
    os._exit(0)

def parent():
    base_url = 'https://hr.tencent.com/position.php?start=%d'
    for i in range(0,900+1,10):
        fullurl = base_url%i
        newpid = os.fork()
        if newpid == 0:
            child(fullurl)
        else:
            pass


if __name__ == '__main__':
    parent()
    time.sleep(2)
    print('运行完毕')