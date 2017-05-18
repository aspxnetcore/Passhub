#!/usr/bin/env python
# encoding:utf-8
from handler.public import (BasePage, BaseApi, Auth)
from fastweb import coroutine
import sys
from utils.tools.randomNum import RandomNum
from utils.tools.times import Time

reload(sys)
sys.setdefaultencoding('utf-8')


class OTPHandler(BasePage):
    @coroutine
    @Auth.authUser
    def get(self):
        self.end('otp/index.html', username=self.get_secure_cookie("user_name"))


class OTPListHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def get(self):
        user_id = self.get_secure_cookie("userId")

        sql = '''
        SELECT
            id,
            group_name,
            group_desc,
            access_id,
            access_key
        FROM
            otp_group
        WHERE
            user_admin_id = %s;
        '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result = self.mysql_passhub_db.fetchall()

        list = []

        for r in result:
            json = {}
            json['id'] = r['id']
            json['group_name'] = r['group_name']
            json['group_desc'] = r['group_desc']
            json['access_id'] = r['access_id']
            json['access_key'] = r['access_key']

            key = RandomNum.make_key(r['access_id'], r['access_key'])

            json['key'] = key

            list.append(json)

        self.end(code='SUC', log=True, **{'result': list})


class OTPShareListHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def get(self):
        user_id = self.get_secure_cookie("userId")

        sql = '''
            SELECT
                otp_group.id,
                otp_group.group_name,
                otp_group.group_desc,
                otp_group.access_id,
                otp_group.access_key
            FROM
                user_otp_list
            JOIN otp_group ON user_otp_list.otp_id = otp_group.id
            WHERE
                user_otp_list.user_id = %s;
        '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result = self.mysql_passhub_db.fetchall()

        list = []

        for r in result:
            json = {}
            json['id'] = r['id']
            json['group_name'] = r['group_name']
            json['group_desc'] = r['group_desc']
            json['access_id'] = r['access_id']
            json['access_key'] = r['access_key']

            key = RandomNum.make_key(r['access_id'], r['access_key'])

            json['key'] = key

            list.append(json)

        self.end(code='SUC', log=True, **{'result': list})


class OTPAddHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def post(self):
        otp_name = self.get_argument('otp_name')
        otp_desc = self.get_argument('otp_desc')

        user_id = self.get_secure_cookie("userId")

        access_id = RandomNum.make_str(10)
        access_key = RandomNum.make_md5number(10)

        sql = '''
        INSERT INTO otp_group (
            user_admin_id,
            group_name,
            group_desc,
            access_id,
            access_key,
            create_time
        )
        VALUES
            (%s, %s, %s, %s, %s, %s);
        '''

        yield self.mysql_passhub_db.start_event()
        yield self.mysql_passhub_db.exec_event(sql, (
            user_id, otp_name, otp_desc, access_id, access_key, Time.get_date_time()))
        yield self.mysql_passhub_db.end_event()

        self.end(code='SUC', log=True, **{'result': 'success'})


class OTPUpdateHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def post(self):
        id = self.get_argument('id')
        otp_name = self.get_argument('otp_name')
        otp_desc = self.get_argument('otp_desc')

        user_id = self.get_secure_cookie("userId")

        sql = '''
            UPDATE otp_group
            SET group_name = %s,
             group_desc =  %s
            WHERE
                id =  %s
            AND user_admin_id =  %s;
        '''

        yield self.mysql_passhub_db.start_event()
        yield self.mysql_passhub_db.exec_event(sql, (otp_name, otp_desc, id, user_id))
        yield self.mysql_passhub_db.end_event()

        self.end(code='SUC', log=True, **{'result': 'success'})


class OTPDelHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def post(self):
        id = self.get_argument('id')
        user_id = self.get_secure_cookie("userId")

        sql = '''
            DELETE
            FROM
                otp_group
            WHERE
                id = %s
            AND user_admin_id = %s;
        '''

        yield self.mysql_passhub_db.start_event()
        yield self.mysql_passhub_db.exec_event(sql, (id, user_id))
        yield self.mysql_passhub_db.end_event()

        self.end(code='SUC', log=True, **{'result': 'success'})


class OTPUserlistHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def get(self):
        user_id = self.get_secure_cookie("userId")

        sql = '''
        SELECT
            id,
            user_name,
            user_mail
        FROM
            hub_user
        WHERE
            id != %s;
        '''

        yield self.mysql_passhub_db.query(sql, user_id)
        result = self.mysql_passhub_db.fetchall()

        list = []

        for r in result:
            json = {}
            json['id'] = r['id']
            json['user_name'] = r['user_name']
            json['user_mail'] = r['user_mail']

            list.append(json)

        self.end(code='SUC', log=True, **{'result': list})


class OTPUserlistsHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def get(self):
        id = self.get_argument("id")

        sql = '''
        SELECT
            hub_user.id,
            hub_user.user_name,
            hub_user.user_mail
        FROM
            otp_group
        JOIN user_otp_list ON otp_group.id = user_otp_list.otp_id
        JOIN hub_user ON user_otp_list.user_id = hub_user.id
        WHERE otp_group.id = %s
        '''

        yield self.mysql_passhub_db.query(sql, id)
        result = self.mysql_passhub_db.fetchall()

        list = []

        for r in result:
            json = {}
            json['id'] = r['id']
            json['user_name'] = r['user_name']
            json['user_mail'] = r['user_mail']

            list.append(json)

        self.end(code='SUC', log=True, **{'result': list})


class OTPUserDelHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def post(self):
        id = self.get_argument("otp_id")
        vals = self.get_argument("vals")

        print id, vals

        b = vals.replace(",", "\",\"")
        b = '"' + b + '"'

        print b

        sql = '''
        DELETE
        FROM
            user_otp_list
        WHERE
            user_id IN (''' + b + ''')
        AND otp_id = %s;
        '''

        yield self.mysql_passhub_db.start_event()
        yield self.mysql_passhub_db.exec_event(sql, id)
        yield self.mysql_passhub_db.end_event()

        self.end(code='SUC', log=True, **{'result': 'success'})


class OTPUserAddHandler(BaseApi):
    @coroutine
    @Auth.authUser
    def post(self):
        id = self.get_argument("otp_id")
        username = self.get_argument("username")

        sql = '''
        SELECT
            id
        FROM
            hub_user
        WHERE
            user_name = %s;
        '''

        yield self.mysql_passhub_db.query(sql, username)
        result = self.mysql_passhub_db.fetchall()

        if result:
            user_id = result[0]['id']
            insert_sql = '''
                INSERT INTO user_otp_list (user_id, otp_id)
                VALUES
                    (%s, %s);
            '''

            yield self.mysql_passhub_db.start_event()
            yield self.mysql_passhub_db.exec_event(insert_sql, (user_id, id))
            yield self.mysql_passhub_db.end_event()

            self.end(code='SUC', log=True, **{'result': 'success'})
        else:
            self.end(code='SUC', log=True, **{'result': 'fail'})
