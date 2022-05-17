#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 练习.py
# @Time      : 2022/5/6 16:49
# @Author    : weilig
'''
1. 定义一个表示时间的类time，他提供下面操作:
    1. time（hours，minutes，seconds）创建一个时间对象
    2. t.hours() t.minutes() t.seconds() 分别返回时间对象t的小时，分钟和秒值
    3. 为 time 对象定义加法和减法操作（用运算符 + 和 -）
    4. 定义时间对象的等于和小于关系运算（用运算符 == 和 <  >）
注意：time类的对象可以采用不同的内部表示。例如，可以给每个对象定义三个数据属性 hours， minutes， seconds ，基于这种表示实现操作。可以用一个属性seconds，构造对象时算出参数相对于基准时间 0:0: 的秒值，同样可以实现所有操作。青葱各方面权衡利弊，选择合适的设计。

'''


class Time:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def add(self):
        '''
        加法
        :return:
        '''
        pass

    def sub(self):
        '''
        减法
        :return:
        '''
        pass


time1 = Time(0, 0, 0)
