# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['lianjia.com']

    def start_requests(self):
        # 初始化的url地址
        start_urls = ['http://bj.lianjia.com/ershoufang/']
        #参数配置
        formdata = {

        }
        # 循环发送请求
        for url in start_urls:
            # 发送post请求
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        url_list = response.xpath('//a[@class="title"]/@href').extract()
        yield scrapy.FormRequest(url=url_list[0], callback=self.parse_item)
        '''
        for url in url_list:
            yield scrapy.FormRequest(url=url,callback=self.parse_item)
        '''

    def parse_item(self,response):
        print('----')
        url_list = response.xpath('//div[@class = "container"]/div[@class = "list"]/div/img/@src').extract()
        title_list = response.xpath('//h1[@class = "main"]/text()').extract()
        item = FirstspiderItem()
        item['image_urls'] = url_list
        item['images'] = title_list
        print(item)
        yield item
