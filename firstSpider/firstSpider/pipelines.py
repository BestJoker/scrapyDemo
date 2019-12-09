# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
'''
Scrapy管道的电影用途
清理HTML数据
验证抓取的数据（检查项目是否包含特定字段）
检查重复（并删除）
将抓取的数据存储在数据库中
'''

class FirstspiderPipeline(object):

    #爬虫开始就会触发这个方法
    def open_spider(self,spider):
        print('爬虫开始')

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
        print(item)
        #可以在这里筛选item
        if (1):
            return item
        else:
            raise DropItem('Missing title in %s' % item)


    #爬虫结束触发这个方法
    def close_spider(self,spider):
        print('爬虫结束')
