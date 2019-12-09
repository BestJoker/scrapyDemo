# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
import json

'''
Scrapy管道的电影用途
清理HTML数据
验证抓取的数据（检查项目是否包含特定字段）
检查重复（并删除）
将抓取的数据存储在数据库中
'''

class FirstspiderPipeline(object):

    '''
    from_crawler(cls, crawler) —— 非必需，也是在启动的时候调用，比
    open_spider早。

    该类方法用来从 Crawler 中初始化得到一个 pipeline 实例；它必须返回一个新的 pipeline
    实例；Crawler 对象提供了访问所有 Scrapy 核心组件的接口，包括 settings 和 signals

    需要传入的参数：
    crawler (Crawler 对象) ： 使用该管道的crawler

     def from_crawler(cls,crawler):
        s = cls()
        repr(s)
    '''




    #爬虫开始就会触发这个方法
    '''
    open_spider(self, spider) -- 非必须实现，为爬虫启动的时候调用

    '''
    def open_spider(self,spider):
        print('爬虫开始')
        #self.file = open('test.json','w')


    '''
    process_item(self, item, spider) -- 必须实现方法
    
    每个 Item Pipeline 组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 
    或是抛出 DropItem 异常，被丢弃的 item 将不会被之后的 pipeline 组件所处理
    
    需要传入的参数为：
    item (Item 对象) ： 被爬取的 item
    spider (Spider 对象) ： 爬取该 item 的 spider
    
    持久化流程：
​    1.爬虫文件爬取到数据后，需要将数据封装到items对象中。
​    2.使用yield关键字将items对象提交给pipelines管道进行持久化操作。
​    3.在管道文件中的process_item方法中接收爬虫文件提交过来的item对象，然后编写持久化存储的代码将item对象中存储的数据进行持久化存储
​    4.settings.py配置文件中开启管道

    '''

    def process_item(self, item, spider):
        print (item['title'])
        #print (item['des'])
        #print (item['round'])
        #print (item['url'])
        #print (item['date'])
        #print ('\n')
        #设置丢弃没有标题的那些item(可以根据自己情况使用一些标准来过滤item)
        if item['title']:
            '''
            #将item变成json字符串，然后写入到文件中
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            '''
            return item
        else:
            raise DropItem('Missing title in %s' % item)



    #爬虫结束触发这个方法
    '''
    close_spider(self, spider) —— 非必需， 为爬虫关闭的时候调用；
    '''
    def close_spider(self,spider):
        print('爬虫结束')
        #self.file.close()
