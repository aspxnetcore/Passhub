#!/usr/bin/env python
# encoding:utf-8
import random
import time
import hashlib
from fastweb import options
import ConfigParser


# 随机数生成
class RandomNum(object):
    @staticmethod
    def make_code(num):
        code_list = []
        for i in range(10):
            code_list.append(str(i))
        myslice = random.sample(code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        return number

    @staticmethod
    def make_number(num):
        code_list = []
        for i in range(10):
            code_list.append(str(i))

        myslice = random.sample(code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        times = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return times + '' + number

    @staticmethod
    def make_md5number(num):
        code_list = []
        for i in range(10):
            code_list.append(str(i))

        myslice = random.sample(code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        times = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        r = times + '' + number
        m2 = hashlib.md5()
        m2.update(r)
        return m2.hexdigest().upper()

    @staticmethod
    def make_str(num):
        code_list = []
        for i in range(10):
            code_list.append(str(i))

        myslice = random.sample(code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        times = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return 'passhub_' + times + '' + number

    @staticmethod
    def make_key(access_id, access_key):
        config_path = options.config
        cf = ConfigParser.ConfigParser()
        cf.read(config_path)

        rule_type = cf.get("key_setting", "rule_type")
        rule_str = cf.get("key_setting", "rule_str")

        s = str(rule_str) + '_' + str(access_id) + '_' + str(access_key) + '_' + str(
            time.strftime("%Y%m%d%H%M", time.localtime(time.time())))

        if str(rule_type) == '0':
            m2 = hashlib.md5()
            m2.update(s)
            md51 = m2.hexdigest().upper()
            m2 = hashlib.md5()
            m2.update(md51)
            md52 = m2.hexdigest().upper()
            return md52[-6:]
        elif str(rule_type) == '1':
            m2 = hashlib.md5()
            m2.update(s)
            md51 = m2.hexdigest().lower()
            m2 = hashlib.md5()
            m2.update(md51)
            md52 = m2.hexdigest().lower()
            return md52[-6:]
        elif str(rule_type) == '2':
            m2 = hashlib.md5()
            m2.update(s)
            md51 = m2.hexdigest().upper()
            m2 = hashlib.md5()
            m2.update(md51)
            md52 = m2.hexdigest().upper()
            s = filter(lambda ch: ch in '0123456789', md52)
            return s[-6:]
        else:
            return '000000'
