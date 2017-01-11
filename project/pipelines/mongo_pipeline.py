#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import uuid
from datetime import datetime
import pymongo


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'spider')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item["uuid"]=str(uuid.uuid1())
        item['createtime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item['pid']=os.getpid()
        self.db[spider.name].insert(dict(item))
        return item