#!/usr/bin/env python
# encoding:utf-8
from fastweb import coroutine
from handler.public import (BasePage, Auth)


class HomeHandler(BasePage):
    @coroutine
    @Auth.authUser
    def get(self):
        user_id = self.get_secure_cookie("userId")

        sql = '''
            SELECT
                COUNT(1) as sum
            FROM
                otp_group
            WHERE
                user_admin_id = %s;
            '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result = self.mysql_passhub_db.fetchall()

        sql = '''
            SELECT
                COUNT(1) as sum
            FROM
                user_otp_list
            WHERE
                user_id = %s;
            '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result1 = self.mysql_passhub_db.fetchall()

        sql = '''
            SELECT
                COUNT(1) as sum
            FROM
                login_log
            WHERE
                type = 1 AND user_id = %s;
            '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result3 = self.mysql_passhub_db.fetchall()

        sql = '''
            SELECT
                COUNT(1) as sum
            FROM
                login_log
            WHERE
                type = 2 AND user_id = %s;
            '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result4 = self.mysql_passhub_db.fetchall()

        json = {}
        json['my_sum'] = result[0]['sum']
        json['share_sum'] = result1[0]['sum']
        json['success_sum'] = result3[0]['sum']
        json['fail_sum'] = result4[0]['sum']

        self.end('home/index.html', username=self.get_secure_cookie("user_name"), json=json)
