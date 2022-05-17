#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 构建一个简单的线性表.py
# @Time      : 2022/5/7 14:02
# @Author    : weilig


class Table:
    def __init__(self, value: list):
        if isinstance(value, list):
            self.count = value
        else:
            raise TypeError('value type error')

    def __len__(self):
        print('len方法触发__len__魔法方法')
        return len(self.count)

    def __str__(self):
        print('print出发了__str__魔法方法')
        res = [str(i) for i in self.count]
        return '{}'.format(res)

    def is_empty(self):
        status = True
        if len(self) > 0:
            status = False
        return status

    def prepend(self, value):
        '''
        头部插入元素
        :param value:
        :return:
        '''
        self.count.insert(0, value)

    def append(self, value):
        '''
        尾部插入元素
        :param value:
        :return:
        '''
        self.count.append(value)

    def insert(self, index, value):
        '''
        指定位置插入元素
        :param index:
        :param value:
        :return:
        '''
        self.count.insert(index, value)

    def del_first(self):
        '''
        删除第一个元素
        :return:
        '''
        self.count.pop(0)

    def del_last(self):
        '''
        删除最后一个元素
        :return:
        '''
        self.count.pop(-1)

    def search(self, value):
        '''
        查找元素
        :return:
        '''
        return self.count.index(value)

    def forall(self):
        '''
        对每个元素执行op操作
        :return:
        '''


table = Table([1, 2, 3])
length = len(table)
print(length)
print(table)
table.prepend(0)
print(table)
table.append(0)
print(table)
table.insert(2, 'g')
print(table)
table.del_first()
print(table)
table.del_last()
print(table)
res = table.search('g')
print(res)
res = table.is_empty()
print(res)
