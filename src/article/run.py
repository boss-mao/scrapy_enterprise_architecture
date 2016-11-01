#!/usr/bin/python
#-*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import huxiu.spiders

process = CrawlerProcess(get_project_settings())
process.crawl(huxiu.spiders.HuXiuArticleSpider)
process.start()