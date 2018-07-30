from urllib import request
import time,random,json

# 爬贴吧的数据
def domnload_douban_json():
    # 存储最终数据的容器
    json_data = ''
    base_url = 'https://movie.douban.com/j/chart/top_list?type={type}&interval_id=100%3A90&action=&start={start}&limit=20'
    type=13
    start=1-1
    end=2
    # 打开文件，先写入一个[
    f = open('./json/'+str(type)+'.json','w',encoding='utf-8')
    for i in range(start,end):
        time.sleep(random.random()*1)
        # 生成完整的请求连接
        full_url = base_url.format(type=type,start=i*20)
        # 发送请求：
        response = request.urlopen(full_url)
        # 处理数据
        data = response.read().decode()
        # 先用json方法转换成列表
        data=json.loads(data)
        if data:
            for move in data:
                json_data += json.dumps(move,ensure_ascii=False)+',\n'
            json_data+','
        else:
            break
    json_data = '[\n'+json_data[:-2]+'\n]'
    f.write(json_data)

# 爬雪球的json数据
def domn_xueqiu_json():
    json_data = '[\n'
    base_url = 'https://xueqiu.com/stock/cata/stocklist.json?page={}&size=30&order=desc&orderby=percent&type=11%2C12&_=1528725074944'
    full_url = base_url.format(1)
    # 构建请求对象
    user_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    ]
    headers = {
        'User-Agent':random.choice(user_list),
        'Cookie': 'aliyungf_tc=AQAAAFvWMUknKQQAWQB5aoI4G/+HNJXQ; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528725028; _ga=GA1.2.1327932955.1528725029; _gid=GA1.2.211366692.1528725029; u=151528725029953; device_id=611cd9d972f701412a42e48419cb980e; s=g9121xve9j; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528725039; __utma=1.1327932955.1528725029.1528725039.1528725039.1; __utmc=1; __utmz=1.1528725039.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=1.1.10.1528725039'
    }
    req = request.Request(full_url,headers=headers)
    # 发送请求
    response = request.urlopen(req)
    datas = response.read().decode()
    datas = json.loads(datas)['stocks']
    for data in datas:
        json_data += json.dumps(data,ensure_ascii=False)+',\n'
    json_data = json_data[:-2] + '\n]'

    with open('./json/xueqiu.json','w',encoding='utf-8') as f:
        f.write(json_data)

if __name__=='__main__':
    # domnload_douban_json()
    domn_xueqiu_json()


