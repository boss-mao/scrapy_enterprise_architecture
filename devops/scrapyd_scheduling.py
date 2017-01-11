#!/usr/bin/python
#-*- coding: utf-8 -*-
import os

import requests
import sys
import settings

def schedule(project, spider,server_url=settings.scrayd_url):
    response=requests.post(server_url+"/schedule.json",{"project":project,"spider":spider})
    response.close()
    return response.text

if __name__ == "__main__":
    print schedule(project="project", spider="dmoz_mai")
