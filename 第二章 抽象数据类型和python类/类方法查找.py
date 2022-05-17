#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 类方法查找.py
# @Time      : 2022/4/8 11:24
# @Author    : weilig
'''
如果一个子类的实例对象出发去调用方法，python解释器需要确定应该调用那个函数。查找过程先从实例对象所属的类开始，如果在这里找到，就采用相应的函数定义，
如果没有找到就到这个父类中去查找。如果还没有找到python解释器就会报告AttributeError异常。
如果所属，定义子类是可以覆盖父类里已有的函数定义。按照上述查找过程，一旦某函数在派生类里重新定义，在其实例对象的方法调用解析中，就不会再去使用父类里原来定义的方法了
假设实例情况：
'''


class B:
    def f(self):
        self.g()

    def g(self):
        print('B.g  called')


class C(B):
    def g(self):
        print('C.g called')


x = B()
x.f()
y = C()
y.f()

'''
当创建B类的实例对象x之后调用x.f(),显然将调用B类的定义的g并打印出“B.g called”。但如果创建一个C类的实例对象y并调用y.f()呢
B.g  called
C.g called
由于C类里没有f的定义，y.f()实际调用的是B类里定义的f。由于在f的定义里出现了调用self.g，现在出现了一个问题：如何确定应该调用的函数g。从程序的正文看，正在执行的方法f的定义出现在类B里，self的类型应该是B。
如果根据这个类型去查找g，就应该找到类B里定义的函数g。采用这种根据静态程序正文去确定被调用方法的规则称为静态约束（利益查关键说法是静态绑定）。但python不这样做，他和多数常见的面向对象语言一样，
基于方法调用时self所表示的那个实例对象的类型去确定应该调用那个g，这种方式称为动态约束
这样，y.f()的执行过程将是：由于y值是C类的实例对象，首先基于它确定实际应该调用的方法函数f。由于C类里没有f的定义，按规则应该到C类的基类中去查找f。在C的基类B里找到了f的定义，因此应该执行它.
下一个问题实在函数f的执行种遇到了调用self.g()。由于当时self的值是C类定义的一个对象，确定g的工作再次从调用对象所属的C类开始进行。由于C类里存在函数g的定义，所以执行C类中的g方法。
在程序设计领域，这种通过动态约束确定调用关系的函数称为虚函数.
'''


'''

Content-Type: application/json; charset=UTF-8
              application/x-www-form-urlencoded; charset=utf-8
              text/html; charset=UTF-8
              text/javascript
'''