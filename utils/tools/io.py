#!/usr/bin/env python
# encoding:utf-8
import os


# IO 读写
class IO(object):
    # 打开文件
    def open(self, PATH):
        result = os.path.exists(PATH)
        if result:
            with open(PATH) as f:
                for line in f:
                    return line
        else:
            return 'file does not exist.'

    # 写入文件
    def write(self, PATH, CODE):
        file = open(PATH, "wb")
        file.write(CODE)
        file.close()
        print 'Installation success.'
        return 'success'
