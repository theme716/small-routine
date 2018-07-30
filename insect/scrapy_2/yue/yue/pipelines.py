# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import pymysql

class YuePipeline(object):
    def process_item(self, item, spider):
        return item

class YuehuipicPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        pic_pathurl = []
        for res in results:
            if res[0]:  # 下载成功
                pic_pathurl.append(res[1]['path'].strip('full/'))
                # print(res[1]['path'])
        pic_pathurl = ','.join(pic_pathurl)

        if item['status'] == '0':
            item['pic_pathurl'] = pic_pathurl
        # print(pic_pathurl)
        return item

class YuehuiMysqlPipeline(object):
    '''
    即存储user数据库，也存储heart数据库，利用多态
    '''
    def open_spider(self,spider):
        self.con = pymysql.connect('127.0.0.1','root','123456','reptile',charset = 'utf8')
        self.cursor = self.con.cursor()

    def process_item(self,item,repider):
        sql,data = item.get_sql()
        try:
            self.cursor.execute(sql,data)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
            print('===========================sql报错==================')
            print(e)
            print('========================='+item["full_url"]+'============================')
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()

