# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['ip138.com']

    def start_requests(self):

        # 初始化的url地址
        start_urls = ['http://2000019.ip138.com/']
        
        #参数配置
        formdata = {

        }
        # 循环发送请求
        for url in start_urls:
            # 发送post请求
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        print(response)
        item = FirstspiderItem()
        data = response.xpath('//body/p[1]/text()').extract()
        print(data)
        #返回item否则不会调用items文件中的方法
        yield item
