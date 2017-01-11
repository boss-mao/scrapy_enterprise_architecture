#!/usr/bin/python
#-*- coding: utf-8 -*-
import os


#删除文件夹
def delete_folder(src):
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