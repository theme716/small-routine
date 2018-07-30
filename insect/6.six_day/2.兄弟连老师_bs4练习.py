from bs4 import BeautifulSoup
import requests
# 发送请求
base_url = 'http://www.itxdl.cn/activity/teacher/teacher_lieibiao/'
response = requests.get(base_url)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    html = response.text
    # 构建bs4对象
    html = BeautifulSoup(html,'lxml')
    # 先查找到老师信息大的模块
    teacher_list = html.select('div.php_jiangshi_liebiao')
    with open('teacher.csv','w',encoding='utf-8') as f:
        for teacher in teacher_list:
            # 提取每个模块里面的一条条信息 并写入文件
            name = teacher.select('h1')[0].text.strip()
            info = teacher.select('p')[0].text
            img = teacher.select('img')[0]['src']
            item = [name,info,img]
            f.write(','.join(item)+'\n')