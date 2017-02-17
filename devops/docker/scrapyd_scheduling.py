#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
from devops import util


def schedule(project, spider):
    result=[]
    for name,target in  util.get_targets().items():
        response=requests.post(target["url"]+"schedule.json",{"project":project,"spider":spider})
        response.close()
        result.append(response.text)
    return result



