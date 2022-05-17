#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 对象计数器.py
# @Time      : 2022/4/8 10:06
# @Author    : weilig

class Countable:
    counter = 0

    def __init__(self, name, *args, **kwargs):
        self.name = name
        Countable.counter += 1

    @classmethod
    def get_count(cls):
        return Countable.counter

    def __del__(self):
        Countable.counter -= 1


a = Countable('a')
a.counter = 0
print(a.get_count())
b = Countable('b')
print(b.get_count())
c = Countable('c')

print(c.get_count())
print(a.get_count())
print(b.get_count())

print(a.counter)
print(b.counter)
print(c.counter)

del c
print(Countable.get_count())

'''
结果依次是：
1
2

3
3
3

3
3
3
从这里反映出，类属性对于所有的对象共享
'''
