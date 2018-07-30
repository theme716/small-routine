import random, time, re, json, os
from urllib import request,parse

base_url = 'http://mce.meilishuo.com/jsonp/get/3?callback=jQuery112405176858786965051_1528897544403&offset=0&frame=2&trace=0&limit=10&endId=0&pid=106888&page={}&_=1528897544410'


# http://mce.meilishuo.com/jsonp/get/3?callback=jQuery112405176858786965051_1528897544403&offset=0&frame=1&trace=0&limit=10&endId=0&pid=106888&page=2&_=1528897544409 HTTP/1.1
# http://mce.meilishuo.com/jsonp/get/3?callback=jQuery112405176858786965051_1528897544403&offset=0&frame=2&trace=0&limit=10&endId=0&pid=106888&page=3&_=1528897544410 HTTP/1.1

def create_headers():
    '''
    :return:返回请求头
    '''
    useragent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(useragent_list)
    }
    return random.choice(useragent_list)


headers = {
    'User-Agent': create_headers(),
}

def rep():
    start = int(input('请输入起始页：'))
    end = int(input('请输入结束页：'))

    if not os.path.exists('./meilishuo_pics'):
        os.makedirs('./meilishuo_pics')
    if not os.path.exists('./meilishuo_json'):
        os.makedirs('./meilishuo_json')
    for page in range(start,end+1):

        # 建立文件
        filename ='./meilishuo_json/'+str(page) + '.json'
        f = open(filename, 'w', encoding='utf-8')
        f.write('[\n')

        full_url = base_url.format(page)
        req = request.Request(full_url, headers=headers)
        response = request.urlopen(req)
        data = response.read().decode()
        pat = re.compile('({".+})')
        data2 = pat.search(data)
        data2 = data2.group()
        data3 = json.loads(data2)
        data4 = data3['data']['list']

        if not os.path.exists('./meilishuo_pics/' + str(page)):
            os.makedirs('./meilishuo_pics/' + str(page))

        for i in range(0,len(data4)):
            # 下载图片
            request.urlretrieve(data4[i]['image'],'./meilishuo_pics/' + str(page)+'/'+str(i+1)+'.jpg')
            # 添加本地图片的键
            data4[i]['picurl'] = data4[i]['image'],'meilishuo_pics/' + str(page)+'/'+str(i+1)+'.jpg'
            # 数据存储进json
            if page == end and i == len(data4)-1:
                f.write(json.dumps(data4[i])+'\n')
            else:
                f.write(json.dumps(data4[i])+',\n')
        f.write(']')
        f.close()

if __name__ == '__main__':
    rep()
