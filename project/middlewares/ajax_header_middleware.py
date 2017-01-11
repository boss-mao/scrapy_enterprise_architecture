#!/usr/bin/python
#-*- coding: utf-8 -*-
import logging

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

logger = logging.getLogger(__name__)
#随即分配UA
class AjaxHeader(UserAgentMiddleware):
    def process_request(self, request, spider):
            request.headers.setdefault('X-Requested-With', 'XMLHttpRequest')

