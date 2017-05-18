#!/usr/bin/env python
# encoding:utf-8
from fastweb.web import Page, Api
from fastweb import coroutine
import sys
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')


class LoginHandler(Page):
    @coroutine
    def get(self):
        if self.get_secure_cookie("userId"):
            self.redirect('/home')

        self.end('index.html')


class LoginCheckHandler(Api):
    @coroutine
    def post(self, *args, **kwargs):
        account = self.get_argument('account')
        passwd = self.get_argument('passwd')

        m2 = hashlib.md5()
        m2.update(passwd)
        md5_passwd = m2.hexdigest().upper()

        sql = '''
            SELECT
                *
            FROM
                hub_user
            WHERE
                user_name = %s
            AND user_passwd = %s;
        '''

        yield self.mysql_passhub_db.query(sql, (account, md5_passwd))
        result = self.mysql_passhub_db.fetch()
        if result:
            self.set_secure_cookie("userId", str(result['id']))
            self.set_secure_cookie("user_name", str(result['user_name']))
            self.set_secure_cookie("user_mail", str(result['user_mail']))

            self.end(**{'status': 'success'})
        else:
            self.end(**{'status': 'fail'})


class LogoutHandler(Page):
    def get(self):
        self.clear_cookie("userId")  # 清除secure cookie
        self.clear_cookie("user_name")  # 清除secure cookie
        self.clear_cookie("user_mail")  # 清除secure cookie
        self.redirect('/')


class Error404(Page):
    def get(self):
        self.render('404.html')
