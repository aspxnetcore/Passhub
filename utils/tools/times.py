#!/usr/bin/env python
# encoding:utf-8

import time


# 当前时间获取
class Time(object):
    @staticmethod
    def get_date_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def get_week():
        a = time.localtime()
        return time.strftime("%w", a)


    @staticmethod
    def get_date_times():
        return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))