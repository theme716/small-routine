from multiprocessing import Pool
import requests

def task(url):
    response = requests.get(url)
    print(response.url)

if __name__ == '__main__':
    # 返回进程池对象：12代表最大同时执行进程数
    pool = Pool(12)

    base_url = 'https://hr.tencent.com/position.php?start=%d'
    for i in range(0,3760+1,10):
        fullurl = base_url%i
        # 在进程池创建进程
        pool.apply_async(func=task,args=(fullurl,))
    # 关闭进程池，进程池中不能再创建新的进程
    pool.close()
    # 等待进程池中所有的进程运行完毕
    pool.join()
