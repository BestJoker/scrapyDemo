# -*- coding: utf-8 -*-
from firstSpider.settings import USER_AGENT_LIST
from firstSpider.settings import IP_LIST
import random


class UserAgentDownloadMiddleware(object):
    def process_request(self,request,spider):
        #随机选取一个
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent
        print ('随机请求头设置 UserAgentDownloadMiddleware:process_request \n',user_agent)



class RandomIpProxyMiddleware(object):

    def process_request(self,request,spider):
        #随机选取ip
        proxy = random.choice(IP_LIST)
        #获取ip
        #proxy = '111.199.188.112:8888'
        ip = 'http://'+proxy
        #print (id)
        #免费代理处理
        #request.meta['proxy'] = ip
