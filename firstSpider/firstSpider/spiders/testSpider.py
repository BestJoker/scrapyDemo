# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['itjuzi.com']
    #初始化的url地址
    start_urls = ['http://www.itjuzi.com/']

    def parse(self, response):

        print(response)

        item = FirstspiderItem()

        #返回item否则不会调用items文件中的方法
        yield item
