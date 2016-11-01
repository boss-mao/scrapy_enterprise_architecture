#!/usr/bin/python
#-*- coding: utf-8 -*-
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

#随即分配UA
class AjaxHeader(UserAgentMiddleware):
    def process_request(self, request, spider):
            request.headers.setdefault('X-Requested-With', 'XMLHttpRequest')

