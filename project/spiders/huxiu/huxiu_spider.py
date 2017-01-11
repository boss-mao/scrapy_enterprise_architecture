#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
import uuid
import scrapy
import time
from scrapy import Selector


class HuXiuArticleSpider(scrapy.spiders.Spider):
    name = "huxiu_article_spider"
    allowed_domains = ['huxiu.com']
    start_urls = [
        "https://www.huxiu.com/"
    ]
    #定义需要抓取的模块。
    #key为虎嗅网用的标识标识哪个模块,value为自己定义的名字。
    tag_map={'1':"24小时","2":"创业维艰"}
    #发送请求时需要的页面隐藏参数
    key="d140dd77460bed7644c5cab76fc0b529"

    # 爬虫入口
    #通过虎嗅网的ajax接口获取文章列表
    def parse(self, response):
        print response.url
        for tag in self.tag_map:
            yield scrapy.FormRequest(url='https://www.huxiu.com/v2_action/article_list',
                                     method="POST",
                                     meta={'tag': tag},
                                     dont_filter=True,
                                     callback=self.parseTotalPage,
                                     errback=self.handle_error,
                                     formdata={"huxiu_hash_code":self.key,"catid":tag,"page":'1'})


    #解析页面总数量
    def parseTotalPage(self,response):
        print response.url
        data = json.loads(response.body_as_unicode())
        tag = response.meta['tag']
        totalPage=data['total_page']
        #由于数据了比较大 所以暂时设置为2页
        pageCount=int(totalPage)+1
        for page in range(1,3):
            print response.url
            yield scrapy.FormRequest(url='https://www.huxiu.com/v2_action/article_list',
                                     method="POST",
                                     meta={'tag': tag},
                                     dont_filter=True,
                                     callback=self.parseInformationUrl,
                                     errback=self.handle_error,
                                     formdata={"huxiu_hash_code": self.key, "catid": tag, "page":str(page)})

    #获取文章url
    def parseInformationUrl(self, response):
        print response.url
        tag = response.meta['tag']
        #由于文章URL在json的html中，所以需要动态解析html
        data = json.loads(response.body_as_unicode())
        for information_url in Selector(text=data['data'], type="html").xpath('//h2/a/@href').extract():
            yield scrapy.Request(dont_filter=True,
                                 url="https://www.huxiu.com"+information_url,
                                 meta={'tag': tag},
                                 callback=self.parseInformationDetail,
                                 errback=self.handle_error)
    #解析文章的内容
    def parseInformationDetail(self,response):
        print response.url
        tag=response.meta['tag']
        tag_name=self.tag_map[tag]

        model={
            "Id": str(uuid.uuid1()),
            "WebsiteName": u"虎嗅网",
            "CreateTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "Type":tag_name,
            "Url":response.url,
            "Title":"".join(response.xpath('//h1[@class="t-h1"]/text()').extract()),
            "Author": "".join(response.xpath('//div[@class="article-wrap"]/div[@class="article-author"]/span[@class="author-name"]/a/text()').extract()),
            "Content": "".join(response.xpath('//div[@id="article_content"]').extract()),
            "PublishTime":"".join(response.xpath('//div[@class="article-time"]/text()').extract())
        }

        return model

    #处理错误
    def handle_error(self, result, *args, **kw):
        print "error url is :%s" % result.request.url
        self.logger.error("error url is :%s" % result.request.url)