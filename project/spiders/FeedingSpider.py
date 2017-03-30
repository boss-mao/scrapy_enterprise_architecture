#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str


class FeedingSpider(RedisSpider):
    """
        客户端推送信息到redis,然后会自动触发该spider
        这个spider一直等待信号且永远不会结束除非手动取消
    """

    redis_key="feeding:start_urls"
    name = "feeding_spider"
    handle_httpstatus_list = [302]

    def make_request_from_data(self, data):
        """
            如果客户端传输不仅仅是url，需要带一些其他参数信息，就需要重写这个方法
        """
        param = json.loads(bytes_to_str(data, self.redis_encoding))
        return scrapy.Request(url=param["url"],dont_filter=True, method="GET",)

    def parse(self, response):
        #spider自己处理302请求，因为一些网站会随机对IP进行验证码校验，如果有代理可以防止验证码随机校验，不断重试直到代理自动切换到其他IP
        if response.status == 302:
            self.logger.info("app retry redirect url:" + response.url)
            response.request.headers["Referer"] = ""
            response.request.dont_filter = True
            return response.request

        print response.text