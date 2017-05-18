# !/usr/bin/python2.7
# *-*coding:utf8*-*

# 分页
class Pager(object):
    ''' 分页 '''

    # 初始化
    def __init__(self, current_page):
        self.current_page = int(current_page)  # 当前页数
        self.pageSize = 10  # 每页显示 10 条数据 可更改
        self.isHavePrePage = False  # 是否有上一页
        self.isHaveNextPage = False  # 是否有下一页

    # 开始 下标
    @property
    def start(self):
        return (self.current_page - 1) * self.pageSize

    # 结束 下标
    @property
    def end(self):
        return self.current_page * self.pageSize

    # 分页总页数
    def total_page(self, count):
        result = count / self.pageSize
        yu = count % self.pageSize
        if yu > 0:
            result = result + 1
        return result
