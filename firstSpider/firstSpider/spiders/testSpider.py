# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['xicidaili.com/']

    def start_requests(self):
        # 初始化的url地址
        start_urls = ['https://www.xicidaili.com/']
        
        #参数配置
        formdata = {

        }
        # 循环发送请求
        for url in start_urls:
            # 发送post请求
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        item = FirstspiderItem()
        ip1 = response.xpath('//tr/td[2]/text()').extract()
        ip2 = response.xpath('//tr/td[3]/text()').extract()
        area = response.xpath('//tr/td[4]/text()').extract()
        lucency_state = response.xpath('//tr/td[5]/text()').extract()
        http_type = response.xpath('//tr/td[6]/text()').extract()
        for i in range(0,len(ip1)):
            new_ip = 'http://' + ip1[i] + ':' + ip2[i]
            item['ip'] = new_ip
            item['http_type'] = http_type[i]
            item['area'] = area[i]
            item['lucency_state'] = lucency_state[i]
            print(new_ip, http_type[i])
            #返回item否则不会调用items文件中的方法
            yield item
