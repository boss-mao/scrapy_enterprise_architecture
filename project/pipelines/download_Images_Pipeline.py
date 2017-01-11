# coding=utf-8
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re
import os
from scrapy.utils.project import get_project_settings
class DownloadImagesPipeline(ImagesPipeline):


    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]+''
        m = re.search(r'[^/].+[jpg|png|gif]', image_guid)
        if m:
            image_guid = m.group()

        dir_path = ''
        settings = get_project_settings()
        root = settings.get('IMAGES_STORE')
        if root != '':
           dir_path = '%s/%s' % (root,info.spider.name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return '%s/%s' % (info.spider.name, image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
