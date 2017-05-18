#!/usr/bin/env python
# encoding:utf-8

from handler.log.log import log

# URL 正则表达式 路由配置
Route = [
    # 登录页面
    (r"/log", log.LogHandler),
    (r"/log/list", log.LogListHandler),
]
