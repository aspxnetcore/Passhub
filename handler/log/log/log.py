#!/usr/bin/env python
# encoding:utf-8
from handler.public import (BasePage, BaseApi, Auth)
from fastweb import coroutine
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


# 平台首页
class LogHandler(BasePage):
    @coroutine
    @Auth.authUser
    def get(self):
        self.end('log/index.html', username=self.get_secure_cookie("user_name"))


class LogListHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def get(self):
        user_id = self.get_secure_cookie("userId")

        sql = '''
        SELECT
            id,
            log_title,
            `type`,
            log_desc,
            create_time
        FROM
            login_log
        WHERE
            user_id = %s
        LIMIT 20;
        '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result = self.mysql_passhub_db.fetchall()

        list = []

        for r in result:
            json = {}
            json['id'] = r['id']
            json['log_title'] = r['log_title']
            json['type'] = r['type']
            json['log_desc'] = r['log_desc']
            json['create_time'] = datetime.datetime.strftime(r['create_time'], '%Y-%m-%d %H:%M:%S')
            list.append(json)

        self.end(code='SUC', log=True, **{'result': list})
