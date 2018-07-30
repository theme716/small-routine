import json,redis,pymysql

def main():
    # 连接redis
    rediscli = redis.StrictRedis(host='127.0.0.1',port='6379',db=2,password='123456')
    # 连接mysql
    mysqlcli = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
    cur = mysqlcli.cursor()
    # 无限循环从redis取数据
    while True:
        source,data = rediscli.blpop(['tencent:items']) #阻塞式从item里弹出一条数据
        # print(source) #b'tencent:items'
        # print(data) #b'{"title": "17520a1\\u5e08(\\u6df1\\u5733)", "location": "\\u6df1\\u5733", "ptype": "\\u8bbe\\u8ba1\\u7c7b", "number": "3"}'
        item = json.loads(data.decode('utf-8'))
        try:
            sql = 'insert into tencent_hr(p_name,p_type,p_num,p_loc) VALUES(%s,%s,%s,%s)'
            data = (item["title"],item["ptype"],item["number"],item["location"])
            cur.execute(sql,data)
            mysqlcli.commit()
            print('插入了','------------',item['title'])
        except Exception as e:
            mysqlcli.rollback()
            print('插入报错',e)
        # break

if __name__ == '__main__':
    main()

''' 数据库中的字段，数据库名是tencent_hr
    id	int	10
    p_name	varchar	255
    p_type	varchar	255
    p_num	int	11
    p_loc	varchar	255
    p_time	date	0
    duty	varchar	1000
    reqment	varchar	1000
    url_id	varchar	255
'''