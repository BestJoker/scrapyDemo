# coding:utf-8

from scrapy import cmdline

#调用爬虫 不输出日志
cmdline.execute('scrapy crawl testSpider --nolog'.split())

#调用爬虫 输出详细日志
#cmdline.execute('scrapy crawl testSpider'.split())
