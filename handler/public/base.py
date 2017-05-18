#!/usr/bin/env python
# encoding:utf-8
from fastweb.web import Page, Api


# 用户是否登录验证
class BasePages(Page):
    def get_current_user(self):
        url = self.request.uri
        is_check = False
        if url:
            urls = url.replace('/public?', '').split('?')[0]
            authList = self.get_secure_cookie("authList")
            m_list = authList.split("||")
            for m in m_list:
                if urls == m.split("&")[2]:
                    is_check = True

        if is_check == False:
            self.redirect('/404')

        return self.get_secure_cookie("userId")


# 用户是否登录验证
class BasePage(Page):
    def get_current_user(self):
        return self.get_secure_cookie("userId")


# 用户是否登录验证
class BaseApi(Api):
    def get_current_user(self):
        return self.get_secure_cookie("userId")
