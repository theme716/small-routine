# -*- coding:utf-8 -*-
import redis,pymysql,json

def main():
    # 建立redis、mysql的连接
    rediscli = redis.StrictRedis(host='127.0.0.1',db=2,password='123456')
    mysqlcli = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='reptile',charset='utf8')
    cursor = mysqlcli.cursor()

    while True:
        # 从redis里面提取数据
        key,data = rediscli.blpop(['lagou:items'])
        item = json.loads(data.decode('utf-8'))
        # {'url': 'https://www.lagou.com/jobs/4747841.html', 'url_id': 'f4ef3fb06aa43c06eab6f6c2e250361c', 'pname': '平面设计师', 'smoney': '7', 'emoney': '12 ', 'location': '广州', 'syear': '3', 'eyear': '5', 'degree': '全职', 'ptype': '全职', 'tags': '广告营销,平面,设计,创意,视觉', 'date_pub': '2018-07-02', 'advantage': '上市公司,弹性工作,晋升空间,发展空间大', 'jobdesc': ['<div>\n        <p>岗位职责：</p>\n<p>1、根据项目的要求完成相关活动、项目等专题平面设计和修改；</p>\n<p>2、能基本独立完成整个项目的全部设计工作；</p>\n<p>3、对客户的设计要求有较强的领悟和理解能力，并能给出相应的设计成果反应；</p>\n<p>4、在预计项目工时内熟练运用设计软件完成上级领导交给的设计工作；</p>\n<p>5、负责平面美工创意、图片优化等设计排版和编辑。</p>\n<p><br></p>\n<p>任职要求：</p>\n<p>1、3年以上工作经验，有扎实的美术功底、良好的创意思维和理解能力；</p>\n<p>2、大专以上学历，广告视觉、平面设计等相关专业；</p>\n<p>3、熟练操作Photoshop/illustrator/Coreldrew等常用设计软件，对图片渲染和视觉效果有较好认识；</p>\n<p>4、具有良好的设计表现力和设计沟通能力、富有团队合作精神和责任感，思维开阔、有想法有创意；</p>\n<p>5、美术、平面设计相关专业或有相关工作经验，熟悉手绘、品牌设计者优先考虑；熟悉微博、微信、互联网平面创意广告、有互联网广告思维的优先！</p>\n        </div>'], 'jobaddr': '广州-天河区-石牌-天河东路67号丰兴广场A栋2506', 'company': '重庆灵狐科技股份有限公司广州分公司', 'spider_name': 'lagou', 'crawl_time': '2018-07-02'}
        try:
            sql = 'insert into lagou_job(url,url_id,pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company,spider_name,crawl_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            data = (item["url"],item["url_id"],item["pname"],item["smoney"],item["emoney"],item["location"],item["syear"],item["eyear"],item["degree"],item["ptype"],item["tags"],item["date_pub"],item["advantage"],item["jobdesc"],item["jobaddr"],item["company"],item["spider_name"],item["crawl_time"])
            cursor.execute(sql,data)
            mysqlcli.commit()
            print('插入成功',item['url'])
        except Exception as e:
            mysqlcli.rollback()
            print('插入失败',e)


if __name__ == '__main__':
    main()