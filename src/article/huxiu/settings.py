# -*- coding: utf-8 -*-
import logging

BOT_NAME = 'article'
SPIDER_MODULES = ['huxiu.spiders']
NEWSPIDER_MODULE = 'huxiu.spiders'

ITEM_PIPELINES = {
    'huxiu.pipelines.json_writer_pipeline.JsonWriterPipeline': 0,
    'huxiu.pipelines.scrapy_mongodb.MongoDBPipeline':None,
    'huxiu.pipelines.image_pipline.ImagePipeline':None
}

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'huxiu.middlewares.rotate_user_agent_middleware.RotateUserAgentMiddleware' :0
}

COOKIES_DEBUG=True
COOKIES_ENABLED=True
DOWNLOAD_DELAY=2
MONGODB_URI = 'mongodb://192.168.1.6:27017'
MONGODB_DATABASE = 'spider'
MONGODB_COLLECTION = 'spider_item'
IMAGES_STORE='D:\\image'

DEFAULT_REQUEST_HEADERS={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection':'keep-alive'
}

# LOG_FILE='log.txt'
# LOG_LEVEL=logging.INFO
ROBOTSTXT_OBEY = True

