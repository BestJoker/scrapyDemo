# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['sina.com.cn']
    #初始化的url地址
    start_urls = ['http://weather.sina.com.cn/china/']

    def parse(self, response):
        item = FirstspiderItem()
        item['city'] = response.xpath('//td[@style = "width:136px;"]/a/text()').extract()
        item['dayDesc'] = response.xpath('//tr/td[@class="wd_cmt_posr"]/p/text()').extract()
        item['dayDesc1'] = response.xpath('//tr/td[@style="width:125px;"]/text()').extract()
        #返回item否则不会调用items文件中的方法
        yield item
