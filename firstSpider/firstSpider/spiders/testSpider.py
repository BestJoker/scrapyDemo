# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['jianshu.com']
    #初始化的url地址
    start_urls = ['http://www.jianshu.com/']

    def parse(self, response):
        item = FirstspiderItem()
        print(response)
        item['content'] = response.xpath('//a[@class="title"]/text()').extract()
        #拿到对应的详细地址后半段list
        addList = response.xpath('//a[@class="title"]/@href').extract()
        array = []
        #循环创建出对应详情的地址，存储到数组中，并赋值给item【'link'】
        for i in range(0,len(addList)):
            new_url = 'http://www.jianshu.com' + addList[i]
            array.append(new_url)
        item['link'] = array
        #返回item否则不会调用items文件中的方法
        yield item
