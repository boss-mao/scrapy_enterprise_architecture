#!/usr/bin/python
#-*- coding: utf-8 -*-
import os

import requests
import sys
import settings

def cancel(project, job,server_url=settings.scrayd_url):
    response=requests.post(server_url+"/cancel.json",{"project":project,"job":job})
    print response.text
    response.close()
    pass

if __name__ == "__main__":
    cancel(project="project", job="6874a24ccb1211e68c8f7427eaf1ebbe")
