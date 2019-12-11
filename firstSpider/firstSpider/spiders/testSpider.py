# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['douban.com']

    def start_requests(self):
        # 初始化的url地址
        start_urls = ['https://movie.douban.com/top250']
        #参数配置
        formdata = {

        }
        # 循环发送请求
        for url in start_urls:
            # 发送post请求
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        item = FirstspiderItem()
        item['rank'] = response.xpath('//div[@class = "pic"]/em/text()').extract()
        item['name'] = response.xpath('//div[@class = "hd"]/a/span[1][@class = "title"]/text()').extract()
        item['score'] = response.xpath('//span[@class = "rating_num"]/text()').extract()
        item['comment_num'] = response.xpath('//div[@class = "star"]/span[4]/text()').extract()
        #返回item否则不会调用items文件中的方法
        yield item
