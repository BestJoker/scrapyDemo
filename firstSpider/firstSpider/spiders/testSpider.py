# -*- coding: utf-8 -*-
import scrapy
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['www.zhipin.com']

    def start_requests(self):
        # 初始化的url地址
        start_urls = ['https://www.zhipin.com/c101210100/h_101210100/?page=1&ka=page-1']
        #参数配置
        formdata = {

        }
        # 循环发送请求
        for url in start_urls:
            # 发送post请求
            yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        item = FirstspiderItem()
        print('结果 %s' % response.body)
        position = response.xpath('//div[@class="job-title"]/text()').extract()
        salary = response.xpath('//span[@class="red"]/text()').extract() #薪资
        print(position)
        print(salary)
        addr = response.xpath('').extract()  # 工作地址
        years = response.xpath('').extract()  # 工作年限
        education = response.xpath('').extract()  # 学历
        company = response.xpath('').extract()  # 招聘公司
        industry = response.xpath('').extract()  # 行业
        nature = response.xpath('').extract()  # 性质：是否上市
        scale = response.xpath('').extract()  # 规模：人数
        publisher = response.xpath('').extract()  # 招牌者
        publisherPosition = response.xpath('').extract()  # 招聘者岗位
        publishDateDesc = response.xpath('').extract()  # 发布时间

        #返回item否则不会调用items文件中的方法
        yield item
