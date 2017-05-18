#!/usr/bin/env python
# encoding:utf-8

from handler.otp.otp import otp

# URL 正则表达式 路由配置
Route = [
    # 登录页面
    (r"/otp", otp.OTPHandler),
    (r"/otp/add", otp.OTPAddHandler),
    (r"/otp/list", otp.OTPListHandler),
    (r"/otp/lists", otp.OTPShareListHandler),
    (r"/otp/update", otp.OTPUpdateHandler),
    (r"/otp/del", otp.OTPDelHandler),
    (r"/otp/userlist", otp.OTPUserlistHandler),
    (r"/otp/userlists", otp.OTPUserlistsHandler),
    (r"/otp/userdel", otp.OTPUserDelHandler),
    (r"/otp/useradd", otp.OTPUserAddHandler),
]
