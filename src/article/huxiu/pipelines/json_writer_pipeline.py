#!/usr/bin/python
#-*- coding: utf-8 -*-
import codecs
import json


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('unicode_escape'))
        return item

    def close_spider(self, spider):
        self.file.close()



