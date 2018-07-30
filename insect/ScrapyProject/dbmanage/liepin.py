# -*- coding:utf-8 -*-
import redis,pymysql,json

def main():
    # 建立redis、mysql的连接
    rediscli = redis.StrictRedis(host='127.0.0.1',db=2,password='123456')
    mysqlcli = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='reptile',charset='utf8')
    cursor = mysqlcli.cursor()

    while True:
        # 从redis里面提取数据
        key,data = rediscli.blpop(['liepin:items'])
        item = json.loads(data.decode('utf-8'))
        try:
            sql = 'insert into lagou_job(url,url_id,pname,smoney,emoney,location,syear,eyear,degree,ptype,date_pub,advantage,jobdesc,jobaddr,company,spider_name,crawl_time,ages,planguage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            data = (item["url"],item["url_id"],item["pname"],item["smoney"],item["emoney"],item["location"],item["syear"],item["eyear"],item["degree"],item["ptype"],item["date_pub"],item["advantage"],item["jobdesc"],item["jobaddr"],item["company"],item["spider_name"],item["crawl_time"],item['ages'],item['planguage'])
            cursor.execute(sql,data)
            mysqlcli.commit()
            print('插入成功',item['url'])
        except Exception as e:
            mysqlcli.rollback()
            print('插入失败',e)

if __name__ == '__main__':
    main()