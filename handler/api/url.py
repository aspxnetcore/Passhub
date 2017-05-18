#!/usr/bin/env python
# encoding:utf-8

from handler.api.api import api

# URL 正则表达式 路由配置
Route = [
    # 登录页面
    (r"/api/auth", api.ApiHandler),
]
