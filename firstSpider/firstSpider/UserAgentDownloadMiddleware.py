# coding:utf-8
from firstSpider.settings import USER_AGENT_LIST
from firstSpider.settings import HTTP_IP_LIST
from firstSpider.settings import HTTPS_IP_LIST
from scrapy import signals
import random

class UserAgentDownloadMiddleware(object):

    def process_request(self,request,spider):
        #随机选取一个
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent
        #print ('随机请求头设置 UserAgentDownloadMiddleware:process_request \n',user_agent)

        #对拦截到请求的url进行判断（协议头到底是http还是https）
        #request.url返回值：http://www.xxx.com
        h = request.url.split(':')[0]
        print('请求是%s类型' % h)
        ip = ''
        if h == 'https':
            ip = random.choice(HTTPS_IP_LIST)
        else:
            ip = random.choice(HTTP_IP_LIST)
        #request.meta['proxy'] = ip
        #print('请求ip为%s' % request.meta['proxy'])
