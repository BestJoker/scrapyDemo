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
        contentList = item['content']
        linkList = item['link']
        #dict(item) 将item转成dic 然后json.dumps转成json字符串
        for i in range(0,len(contentList)):
            content = contentList[i]
            link = linkList[i]
            print(link)
            print(content)
        return item

        '''
        ①如果不满意可以DropItem，抛出异常

            if len(content) > 20:
                return item
            else:
                raise DropItem('Missing short content')
        ②存储成文件
        ③去重
        一个用于去重的过滤器，丢弃那些已经被处理过的item。
        让我们假设我们的item有一个唯一的id，但是我们spider返回的多个item中包含有相同的id:
            def __init__(self):
            self.ids_seen = set()
    
        def process_item(self, item, spider):
            if item['id'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['id'])
                return item
        ④启用一个Item
        为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置，就像下面这个例子:

        ITEM_PIPELINES = {
            'myproject.pipelines.PricePipeline': 300,
            'myproject.pipelines.JsonWriterPipeline': 800,
        }
        分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。


        '''






    #爬虫结束触发这个方法
    def close_spider(self,spider):
        print('爬虫结束')
