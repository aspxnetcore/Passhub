#!/usr/bin/python2.7
# *-* coding:utf-8 *-*

from fastweb import options
from fastweb.loader import app
from fastweb.web import start_server
from fastweb.pattern import AsynPattern
import os

options.define('port', default=8085, help='this is default port', type=int)

config_path = os.getcwd() + '/config.ini'

options.define('config', default=config_path, help='this is default config path', type=str)

if __name__ == '__main__':
    options.parse_command_line()
    app.load_recorder(os.getcwd() + '/passhub-info.log')
    app.load_configuration(path=options.config)
    app.load_component(pattern=AsynPattern)
    app.load_errcode()

    from handler.system import url as system_url
    from handler.otp import url as otp_url
    from handler.log import url as log_url
    from handler.api import url as api_url

    handlers = []

    handlers[-1:-1] = system_url.Route
    handlers[-1:-1] = otp_url.Route
    handlers[-1:-1] = log_url.Route
    handlers[-1:-1] = api_url.Route

    WEB_CONFIG = {
        # 'debug': True,  # 开发模式
        'xheaders': True,
        'gzip': True,  # 支持gzip压缩
        'autoescape': None,  # 禁用自动转义
        'template_path': os.getcwd() + '/templates/',  # 模板文件目录
        'static_path': os.getcwd() + "/static/",  # 静态文件目录配置
        'static_url_prefix': '/static/',  # 静态文件缓存
        'cookie_secret': "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",  # cookie生成秘钥的随机字符串
        'xsrf_cokkies': True,  # 使用CSRF防御
        "login_url": "/index"  # 登录入口
    }

    start_server(options.port, handlers, **WEB_CONFIG)
