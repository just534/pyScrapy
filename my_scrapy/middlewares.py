# -*- coding: utf-8 -*-

import random
from .settings import User_Agents

class UserAgentMiddleware(object):
    def process_request(self,request,spider):
        random_ua=random.choice(User_Agents)
        request.headers['USER-AGENT']=random_ua

    # def process_response(self,request,response,spider):
    #     print("#"*50)
    #     print(request.headers['USER-AGENT'])
    #     return response

class ProxyMiddleware(object):设置代理中间件
    def process_request(self,request,spider):
        proxy={"http://192.168.0.1:8000"}
        request.meta['proxy']=proxy