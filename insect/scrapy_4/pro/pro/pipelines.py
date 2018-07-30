# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ProPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.connect('127.0.0.1', 'root', '123456', 'reptile', charset='utf8')
        self.cursor = self.con.cursor()

    def process_item(self,item,spider):
        sql  = 'insert into proxy(host,port) VALUES(%s,%s)'
        data = [item['host'],item['port']]
        try:
            self.cursor.execute(sql,data)
            self.con.commit()
            print(data)
        except Exception as e:
            print('========================报错======================')
            print(e)
            print(sql)
            print(data)
            print('==================================================')
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.con.close()