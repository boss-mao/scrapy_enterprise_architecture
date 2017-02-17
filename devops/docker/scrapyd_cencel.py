#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
from devops import util


def cancel(project, job):
    result = []
    for index in range(0,2):
        for name, target in util.get_targets().items():
            response = requests.post(target["url"] + "cancel.json", {"project": project, "job": job})
            response.close()
            result.append(response.text)
    return result


