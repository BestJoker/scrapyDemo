# coding:utf-8

from scrapy import cmdline

if (1):
    # 调用爬虫 不输出日志
    cmdline.execute('scrapy crawl testSpider --nolog'.split())
else:
    # 调用爬虫 输出详细日志
    cmdline.execute('scrapy crawl testSpider'.split())



