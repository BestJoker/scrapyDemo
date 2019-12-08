# -*- coding: utf-8 -*-
import scrapy
import json
import random
import numpy as np
import pandas as pd
import datetime
from firstSpider.items import FirstspiderItem

class TestspiderSpider(scrapy.Spider):
    #爬虫的名字，必须是唯一的
    name = 'testSpider'
    #允许的域名，限制不会乱跑到其他域名上去了
    allowed_domains = ['itjuzi.com']
    # 初始化的url地址
    start_urls = ['http://www.itjuzi.com/api/newsletter']

    def start_requests(self):
        #生成指定范围的日期
        dateList = pd.date_range(start='2019-11-06',end='2019-11-08')
        print ('请求日期列表%s'%str(dateList.date))
        for datetime in dateList:
            #获取timestamp的日期，将日期转换成字符串
            date = datetime.date()
            #设置post参数
            formdata = {
                'time':str(date)
            }
            #循环发送请求
            for url in self.start_urls:
                #发送post请求
                yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.parse)

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
