#!/usr/bin/python
#-*- coding: utf-8 -*-
import scrapyd_cencel
from devops import scrapyd_deploy
from devops import scrapyd_scheduling


def main():
     #部署整个工程
    # scrapyd_deploy.deploy()
    #运行spider
    # print scrapyd_scheduling.schedule(project="lawyer", spider="wenshu_all_spider")
    # 取消运行spder 执行三次
    # print scrapyd_cencel.cancel(project="lawyer",job="7c836e66f36311e681dc0242c0a80002")
    pass


if __name__ == "__main__":
    main()

