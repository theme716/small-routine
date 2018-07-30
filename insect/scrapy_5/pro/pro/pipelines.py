# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ProPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        sql,data = item.get_sql()
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
            print(data[1])
        except Exception as e:
            self.conn.rollback()
            print('=====================mysql报错================')
            print(sql)
            print(data)
            print(e)
            print('========================================')

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class LagouPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self,item,spider):
        sql,data = item.get_sql()
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
            print(data[0],data[2])
        except Exception as e:
            print('=========================sql报错========================')
            print(e)
            print(sql)
            print(data)
            print('-------------------------------------------------------')
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
