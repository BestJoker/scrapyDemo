# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem
import json

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['itjuzi.com']
    # 初始化的url地址
    start_urls = ['http://www.itjuzi.com/api/newsletter']

    def start_requests(self):
        #设置post参数
        formdata = {
            'time':'2019-12-07'
        }
        for url in self.start_urls:
            #发送post请求
            yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse,dont_filter=True)

    def parse(self, response):
        #将爬取到的json字段转换成dic的数据类型
        res = json.loads(response.body_as_unicode())
        print(res)
        item = FirstspiderItem()
        #返回item否则不会调用items文件中的方法
        for contentItem in res['data']:
            item['title'] = contentItem['title']
            item['des'] = contentItem['des']
            item['round'] = contentItem['round']
            item['url'] = contentItem['url']
            item['date'] = contentItem['date']
            yield item
