# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import json,pymysql

class ProPipeline(object):
    def process_item(self, item, spider):
        return item
# 自定义的保存图片的管道，添加了往item中添加图片名字段的功能
class BaiheImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        pic_pathurl = []
        for res in results:
            if res[0]:#下载成功
                pic_pathurl.append(res[1]['path'].strip('full/'))
                print(res[1]['path'])
        pic_pathurl = ','.join(pic_pathurl)
        item['pic_pathurl'] = pic_pathurl
        return item

# 保存入数据库的管道
class BaiheMysqlPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.connect('127.0.0.1','root','123456','reptile',charset='utf8')
        self.cursor = self.con.cursor()
    def process_item(self,item,spider):
        sql,data = item.get_sql()
        try:
            self.cursor.execute(sql,data)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print('============================报错===========================')
            print(e)
            print('=============================='+item["one_url"]+'=============================')

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()
