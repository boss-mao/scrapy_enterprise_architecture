#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from scrapy.utils.conf import get_config


def delete_folder(src):
    """删除文件夹"""

    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


def get_targets():
    "获取所有的部署服务器地址"
    cfg = get_config()
    baset = dict(cfg.items('deploy')) if cfg.has_section('deploy') else {}
    targets = {}
    if 'url' in baset:
        targets['default'] = baset
    for x in cfg.sections():
        if x.startswith('deploy:'):
            t = baset.copy()
            t.update(cfg.items(x))
            targets[x[7:]] = t
    return targets


