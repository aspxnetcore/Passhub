#!/usr/bin/env python
# encoding:utf-8
from handler.public import (BaseApi)
from fastweb import coroutine
import sys
from utils.tools.randomNum import RandomNum

reload(sys)
sys.setdefaultencoding('utf-8')


# 平台首页
class ApiHandler(BaseApi):
    @coroutine
    def post(self):
        access_id = self.get_argument('access_id')
        access_key = self.get_argument('access_key')

        key = RandomNum.make_key(access_id, access_key)

        self.end(code='SUC', log=True, **{'result': key})
