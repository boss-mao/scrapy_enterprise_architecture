#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import  scrapyd_deploy
import  scrapyd_scheduling
import scrapyd_cencel
from scrapy.utils.conf import get_config, closest_scrapy_cfg

from devops import util

def main():
    # 部署整个工程
    scrapyd_deploy.deploy()
    # 运行spider
    print scrapyd_scheduling.schedule(project="project", spider="huxiu_article_spider")
    # 取消运行spder 执行三次
    # scrapyd_cencel.main(project="project",job="cf844626d17b11e697027427eaf1ebbe")


if __name__ == "__main__":
    main()

