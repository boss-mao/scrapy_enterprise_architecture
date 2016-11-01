# -*- coding: utf-8 -*-
import os
import urllib
from huxiu import settings

#处理图片的pipeline
# 爬虫爬取图片时有两种处理方案：
# 1. 如单个图片比如有个网站的logo,可以放到上一个pipline的model中，上一pipline处理完后，由ImagePipeline处理
# 2. 如果爬取一片文章时有多个图片，可以先将所有图片解析出来然后递归爬取(动态替换爬取得链接)或先将文章写到数据库后再爬取。
class ImagePipeline(object):
    image_ext_names=['jpg','png','gif','jpeg']

    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, "201610")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_ext_name=''
        for key in self.image_ext_names:
            if(key in item['url']):
                file_ext_name=key

        file_name=item['Id']+'.'+file_ext_name
        file_path = '%s/%s' % (dir_path, file_name)
        if os.path.exists(file_name):
            return

        with open(file_path, 'wb') as file_writer:
            conn = urllib.urlopen(item['url'])
            file_writer.write(conn.read())
        file_writer.close()

        return item

