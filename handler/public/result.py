#!/usr/bin/env python
# encoding:utf-8
import json


# 返回结果,封装成 json
class Result(object):
    def __init__(self, status='success', result='success', code='200'):
        self.status = status
        self.result = result
        self.code = code

        self.jsons = {}
        self.jsons['status'] = status
        self.jsons['code'] = code

    def makeToJson(self):
        self.jsons['result'] = self.result
        return json.dumps(self.jsons)
