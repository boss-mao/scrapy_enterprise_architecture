#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import settings

def listprojects(server_url=settings.scrayd_url):
    response=requests.get(server_url+"/listprojects.json")
    response.close()
    return response.text

def listversions(project,server_url=settings.scrayd_url):
    response = requests.get(server_url+"/listversions.json?project="+project)
    response.close()
    return response.text

def listspiders(project,server_url=settings.scrayd_url):
    response = requests.get(server_url+"/listspiders.json?project="+project)
    response.close()
    return response.text

def listjobs(project,server_url=settings.scrayd_url):
    response = requests.get(server_url+"/listjobs.json?project="+project)
    response.close()
    return response.text

if __name__ == "__main__":
    print listjobs("project")
