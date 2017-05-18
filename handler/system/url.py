#!/usr/bin/env python
# encoding:utf-8

from handler.system.home import home
from handler.system.login import login

# URL 正则表达式 路由配置
Route = [
    # 登录页面
    (r"/", login.LoginHandler),
    (r"/index", login.LoginHandler),
    (r"/logout", login.LogoutHandler),
    # 登录接口
    (r"/loginCheck", login.LoginCheckHandler),
    # 平台首页
    (r"/home", home.HomeHandler),
]
