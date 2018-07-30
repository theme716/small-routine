from urllib import request,parse
import random,time,os


tieba_name = input('请输入要爬取的贴吧:')
start_page = int(input('请输入开始页码：'))
end_page = int(input('请输入结束页码：'))

def reptile():
    global start_page
    tieba = {
        'kw':tieba_name
    }
    # url
    tieba_url  = 'https://tieba.baidu.com/f?'+ parse.urlencode(tieba) +'&ie=utf-8&pn='
    while start_page <= end_page:
        base_url = tieba_url + str((start_page - 1)*50)
        print(start_page)
        headers_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        ]
        headers = {
            'User-Agent':random.choice(headers_list)
        }
        #构建请求对象
        req = request.Request(base_url,headers=headers)
        # 发送请求
        response = request.urlopen(base_url).read().decode()

        dirname = tieba_name + '/'
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        filename = str(start_page) + '.html'
        with open(os.path.join(dirname,filename), 'w', encoding='utf-8') as f:
            f.write(response)
            # 加入随机事件，防止被禁
            time.sleep(random.random()*1)
        start_page += 1


if __name__=='__main__':
    reptile()



