#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 1.1.1 程序开发过程.py
# @Time      : 2022/3/24 10:04
# @Author    : weilig
'''
求一个非负实数的平方根  y*y=x, 给定x求y
分析：
    1. 对于给定的数值，即使它只包含有穷位小数，其平方根通常也是个无理数, (类似2的平方根 2**0.5)
    2. 根据上一条分析， | y*y-x | < e (e 允许误差), y为无理数 y*y-x会无线趋近于0但始终不等于0 , e假设为 1e-6 (10的负6次方  10**-6 = 0.000001)
    3. 通过牛顿迭代法 z=(x+x/y)/2
    4. 将z作为y值带入到2中继续计算直到表达式成立
'''


def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2

    return y


res = sqrt(4)
print(res)
print(2e+6)
