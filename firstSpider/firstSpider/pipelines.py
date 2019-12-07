# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
import json

class FirstspiderPipeline(object):

    #爬虫开始就会触发这个方法
    def open_spider(self,spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        #假设content是标题
        print (item['title'])
        print (item['des'])
        print (item['round'])
        print (item['url'])
        print (item['date'])
        return item


    #爬虫结束触发这个方法
    def close_spider(self,spider):
        print('爬虫结束')
