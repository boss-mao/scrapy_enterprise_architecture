#!/usr/bin/python
#-*- coding: utf-8 -*-
import os


BOT_NAME = 'project'
SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'

spider_env=os.getenv("SPIDER_ENV", "dev")
#生产环境配置
if spider_env == "product":
    from project.settings.product import *
#开发环境配置
else :
    from project.settings.dev import *







