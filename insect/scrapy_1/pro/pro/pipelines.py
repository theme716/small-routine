# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json,os,time,random
import requests

class Scrapy1TestPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def __init__(self):
        self.fname = 'default.json'

    def open_spider(self,spider):
        print('爬虫开始执行')
        self.f = open(self.fname,'w',encoding='utf-8')

    def process_item(self,item,spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False) + ',\n')
        return item
    def close_spider(self,spider):
        print('爬虫结束执行')

# pipeline,item,就是爬虫文件里面return出来的那个，spider就是spider
class TeacherPipeline(JsonPipeline):
    def __init__(self):
        self.fname = 'teacher.json'

class XiCiPipeline(JsonPipeline):

    def __init__(self):
        self.fname = 'xici.json'

class AnjukePipeline(JsonPipeline):
    def __init__(self):
        self.fname = 'anjuke.json'
    def process_item(self,item,spider):
        print('-------------------------------------------------------------')
        self.f.write(json.dumps(dict(item),ensure_ascii=False) + ',\n')

        h_img_room = item['h_img_room']
        dir_path = './pic/'+str(item['h_id'])+ '/' + '室内'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for link_room in h_img_room:
            pic_name = link_room.replace('https://','')
            end = pic_name.rfind("?")
            pic_name = pic_name[:end]
            response = requests.get(link_room)

            data = response.content
            dir_name = dir_path+'/'+str(time.time()+random.randrange(10000))+'.jpg'
            with open(dir_name,'wb') as f:
                f.write(data)
            print(dir_name)

        h_img_hx = item['h_img_hx']
        dir_path2 = './pic/'+str(item['h_id'])+ '/' + '户型'
        if not os.path.exists(dir_path2):
            os.makedirs(dir_path2)
        for link_hx in h_img_hx:
            pic_name = link_hx.replace('https://','')
            end = pic_name.rfind("?")
            pic_name = pic_name[:end]
            response = requests.get(link_hx)
            data = response.content
            dir_name = dir_path2+'/'+str(time.time()+random.randrange(10000))+'.jpg'
            with open(dir_name,'wb') as f:
                f.write(data)
            print(dir_name)


        h_img_environment = item['h_img_environment']
        dir_path3 = './pic/'+str(item['h_id'])+ '/' + '环境'
        if not os.path.exists(dir_path3):
            os.makedirs(dir_path3)
        for link_environment in h_img_environment:
            pic_name = link_environment.replace('https://','')
            end = pic_name.rfind("?")
            pic_name = pic_name[:end]
            response = requests.get(link_environment)
            data = response.content
            dir_name = dir_path3+'/'+str(time.time()+random.randrange(10000))+'.jpg'
            with open(dir_name,'wb') as f:
                f.write(data)
            print(dir_name)


        print('========================================================================')
        return item
