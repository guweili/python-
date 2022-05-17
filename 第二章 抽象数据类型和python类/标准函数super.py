#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 标准函数super.py
# @Time      : 2022/4/8 13:45
# @Author    : weilig
'''
python提供了一个内置函数super，他把用在派生类的方法定义里，就是要求从这个类的直接父类开始做属性检索。采用super函数而不直接写具体父类的名字，产生的查找过程更加灵活。
如果直接写积累的名字，无论在什么情况下执行，总是调用该父类的方法，而如果写super，python解释器将根据当前类的情况去找到相应的基类，自动确定究竟是应该使用那个父类的属性。
如果在一个方法函数的定义里出现这个调用语句，执行到这个语句时，python解释器就会从这个对象所属类的基类开始，按照上面介绍的属性检索规则去查找函数m。
下面是一段用于说明相关问题的简单代码：
'''


class Book(object):
    """
    书的基类
    """

    def __init__(self, book_id):
        self._id = book_id
        print('初始化Book')

    def print(self):
        """
        打印信息
        :return:
        """
        print('Book')
        print('id:{}'.format(self._id))


class ToolBook(Book):
    """
    工具类书
    """

    def __init__(self, book_id, name):
        print('开始初始化ToolBook')
        super(ToolBook, self).__init__(book_id)
        self._name = name
        print('初始化完成ToolBook')

    def print(self):
        """
        打印信息
        :return:
        """
        print('ToolBook')
        print('id:{}'.format(self._id))


class ScienceBook(Book):
    """
    科学类书
    """

    def __init__(self, book_id):
        print('开始初始化ScienceBook')
        super(ScienceBook, self).__init__(book_id)
        print('初始化完成ScienceBook')

    def print(self):
        """
        打印信息
        :return:
        """
        print('ScienceBook')
        print('id:{}'.format(self._id))


# # 第一种
# class MyBook(ToolBook, ScienceBook):
#     """
#     我感兴趣的书籍类型
#     """
#
#     def __init__(self, book_id, name):
#         print('开始初始化MyBook')
#         super(MyBook, self).__init__(book_id, name)
#         print('初始化完成MyBook')
#
#     def print(self):
#         """
#         打印信息
#         :return:
#         """
#         print('MyBook')
#         super().print()


# 第二种
class MyBook(ToolBook):
    """
    我感兴趣的书籍类型
    """

    def __init__(self, book_id, name):
        print('开始初始化MyBook')
        super(MyBook, self).__init__(book_id, name)
        print('初始化完成MyBook')

    def print(self):
        """
        打印信息
        :return:
        """
        print('MyBook')
        super().print()


# 第三种
class YouBook(ToolBook, ScienceBook):
    """
    我感兴趣的书籍类型
    """

    def __init__(self, book_id):
        print('开始初始化YouBook')
        super(ScienceBook, self).__init__(book_id)  # 触发指定父类的构造方法
        print('初始化完成YouBook')

    def print(self):
        """
        打印信息
        :return:
        """
        print('YouBook')
        super().print()


if __name__ == '__main__':
    # 类的mro列表查询
    print('类MyBook的mro列表：{}'.format(MyBook.mro()))
    print('------------------')

    # 调用初始化函数
    python_book = MyBook('ASW123', 'python_book')
    print('------------------')
    # 类的函数调用
    python_book.print()
    print('------------------')

    # 第三种 类的mro列表查询
    print('类MyBook的mro列表：{}'.format(YouBook.mro()))
    print('------------------')
    # 调用初始化函数
    you_book = YouBook('YouBook123')
    print('------------------')
    # 类的函数调用
    you_book.print()
    print('------------------')
'''
第一种执行结果:
类MyBook的mro列表：[<class '__main__.MyBook'>, <class '__main__.ToolBook'>, <class '__main__.ScienceBook'>, <class '__main__.Book'>, <class 'object'>]
------------------
开始初始化MyBook
开始初始化ToolBook
开始初始化ScienceBook
初始化Book
初始化完成ScienceBook
初始化完成ToolBook
初始化完成MyBook
------------------
MyBook
ToolBook
id:ASW123
------------------

从代码输出结果可以看出MyBook类super调用先访问第一个ToolBook，然后ToolBook的super调用访问其他兄弟类ScienceBook，
最后兄弟类访问完后，ScienceBook类super再去访问Book

#############################################################
第二种执行结果:
类MyBook的mro列表：[<class '__main__.MyBook'>, <class '__main__.ToolBook'>, <class '__main__.Book'>, <class 'object'>]
------------------
开始初始化MyBook
开始初始化ToolBook
初始化Book
初始化完成ToolBook
初始化完成MyBook
------------------
MyBook
ToolBook
id:ASW123
------------------
'''

'''
二、super调用形式
super(Type, 实例)
super()
第1种调用方式中实例必须是Type类型或其子类，第2种调用方式会将当前类指定为Type，并将self指定为实例。
新增一个类如【代码块4】，super可以绕过直接基类访问间接基类。
代码块4


类MyBook的mro列表：[<class '__main__.YouBook'>, <class '__main__.ToolBook'>, <class '__main__.ScienceBook'>, <class '__main__.Book'>, <class 'object'>]
------------------
开始初始化YouBook
初始化Book
初始化完成YouBook
------------------
YouBook
ToolBook
id:YouBook123
------------------
'''
