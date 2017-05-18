#!/usr/bin/env python
# encoding:utf-8
from tornado import httputil
import functools
import urlparse
from urllib import urlencode


# http 错误信息
class HTTPError(Exception):
    def __init__(self, status_code=500, log_message=None, *args, **kwargs):
        self.status_code = status_code
        self.log_message = log_message
        self.args = args
        self.reason = kwargs.get('reason', None)
        if log_message and not args:
            self.log_message = log_message.replace('%', '%%')

    def __str__(self):
        message = "HTTP %d: %s" % (
            self.status_code,
            self.reason or httputil.responses.get(self.status_code, 'Unknown'))
        if self.log_message:
            return message + " (" + (self.log_message % self.args) + ")"
        else:
            return message


# 装饰器 判断是否登录
class Auth(object):
    @staticmethod
    def authUser(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.current_user:
                if self.request.method in ("GET", "HEAD"):
                    url = self.get_login_url()
                    if "?" not in url:
                        if urlparse.urlsplit(url).scheme:
                            next_url = self.request.full_url()
                        else:
                            next_url = self.request.uri
                        url += "?" + urlencode(dict(next=next_url))
                    self.redirect(url)
                    return
                raise HTTPError(403)
            return method(self, *args, **kwargs)

        return wrapper
