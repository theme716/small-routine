from bs4 import BeautifulSoup
import requests
from urllib import request
from mysql import Mysql

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
db = Mysql()

def parse_detail(response,item):

    response.encoding = response.apparent_encoding
    html = response.text
    html = BeautifulSoup(html,'lxml')
    info = html.select('ul.squareli')
    duty = info[0].select('li')
    duty = '--'.join([one_li.text for one_li in duty])
    reqment = info[1].select('li')
    reqment = '--'.join([one_li.text for one_li in reqment])
    item['duty'] = duty
    item['reqment'] = reqment
    sql  = 'insert into tencent_hr(p_name,p_type,p_num,p_loc,p_time,duty,reqment,url_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    data = (item['p_name'],item['p_type'],item['p_num'],item['p_loc'],item['p_time'],item['duty'],item['reqment'],item['url_id'])
    db.execute(sql,data)

def get_list():
    base_url = 'https://hr.tencent.com/position.php?start=%d'
    for i in range(0,90+1,10):
        fullurl = base_url%i
        response = requests.get(fullurl,headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            html = response.text

            # 提取详情页链接
            html = BeautifulSoup(html,'lxml')
            tr_list = html.select('table.tablelist tr')[1:-1]
            for tr in tr_list:
                p_info = tr.select('td')
                p_name = p_info[0].a.text
                url_id = p_info[0].a['href']
                url_id = request.urljoin(base_url,url_id)
                p_type = p_info[1].text
                p_num = p_info[2].text
                p_loc = p_info[3].text
                p_time = p_info[4].text

                item = {
                    'p_name':p_name,
                    'url_id':url_id,
                    'p_type':p_type,
                    'p_num':p_num,
                    'p_loc':p_loc,
                    'p_time':p_time
                }
                #发起详情页请求
                response = requests.get(url_id,headers=headers)
                # 详情页请求处理及记入数据库
                if response.status_code == 200:
                    # response.encoding = response.apparent_encoding
                    # print(response.text)
                    parse_detail(response,item)

if __name__ == '__main__':
    get_list()