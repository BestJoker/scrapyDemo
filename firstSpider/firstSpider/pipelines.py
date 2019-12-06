# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstspiderPipeline(object):

    #爬虫开始就会触发这个方法
    def open_spider(self,spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        #假设content是标题
        content = item['content']
        link = item['link']
        for i in range(0,len(content)):
            print(item['content'][i])
            print(item['link'][i])
        return item

    #爬虫结束触发这个方法
    def close_spider(self,spider):
        print('爬虫结束')
