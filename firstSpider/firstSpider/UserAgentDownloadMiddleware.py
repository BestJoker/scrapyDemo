# -*- coding: utf-8 -*-
from firstSpider.settings import USER_AGENT_LIST
import random


class UserAgentDownloadMiddleware(object):

    def process_request(self,request,spider):
        #随机选取一个
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent
        print ('随机请求头设置 UserAgentDownloadMiddleware:process_request \n',user_agent)
