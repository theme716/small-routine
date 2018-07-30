from urllib import request
import os,time

# 下载图片的方法：
# 方法一：
# 使用request.urlretrieve() 第一个参数是图片url,第二个是存储图片的url
def download_pic(img_url='https://imgsa.baidu.com/forum/w%3D580/sign=a22166c077cb0a4685228b315b62f63e/9f4778899e510fb3a1f6f3add533c895d0430ca3.jpg'):
    if not os.path.exists('./imgs/'):
        os.makedirs('imgs')
    file_name = str(time.time())+'.'+img_url.split('.')[-1]

    request.urlretrieve(img_url,'./imgs/'+file_name)
# 方法二：
def download_pic_2(img_url='https://imgsa.baidu.com/forum/w%3D580/sign=b3eabddd9d2397ddd679980c6983b216/81938518367adab49c3f9f7987d4b31c8601e4ac.jpg'):
    if not os.path.exists('./imgs/'):
        os.makedirs('imgs')
    file_name ='./imgs/'+str(time.time()) + '.'+img_url.split('.')[-1]

    response = request.urlopen(img_url)
    img = response.read()
    with open(file_name,'wb') as f:
        f.write(img)
# 下载视频：
def download_video():
    # 方法一 ：
    request.urlretrieve('https://f.us.sinaimg.cn/0012dCnwlx07lay5sObu010402006AOG0k010.mp4?label=mp4_hd&template=844x480.28&Expires=1528721424&ssig=Xt7ckL1let&KID=unistore,video','./imgs/c.mp4',report)
    # 方法二：
    # response = request.urlopen('https://f.us.sinaimg.cn/0012dCnwlx07lay5sObu010402006AOG0k010.mp4?label=mp4_hd&template=844x480.28&Expires=1528721424&ssig=Xt7ckL1let&KID=unistore,video')
    # vedio = response.read()
    # with open('./imgs/b.mp4','wb') as f:
    #     f.write(vedio)


def report(a,b,c):
    per = 100.0 * a * b / c
    if per>100:
        per=100

    print('%.1f%%'%per)

if __name__=='__main__':
    # download_pic_2()
    # download_pic()
    download_video()


