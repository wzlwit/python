# 简介Python之super的用法及原理
# https://blog.csdn.net/nirendao/article/details/48863215

# NOTE:  super() more likely make diamond inheritance with a sturcture of linear inheritance. 

""" 
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
"""

"""
1. inst负责生成MRO的list；
2. 定位到当前cls在MRO中的位置，然后后移一位，返回此处的类；

MRO就是Method Resolution Order
"""


class A(object):
    def __init__(self):
        print("In A's __init__()")


class B(A):
    def __init__(self):
        print("Enter B's __init__()")
        super(B, self).__init__()
        print("Leave B's __init__()")


class C(A):
    def __init__(self):
        print("Enter C's __init__()")
        super(C, self).__init__()
        print("Leave C's __init__()")


class D(B, C):
    pass


d = D()
print(d.__class__.__mro__)


# output:
"""
$ python test_super.py
Enter B's __init__()
Enter C's __init__()
In A's __init__()
Leave C's __init__()
Leave B's __init__()
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
————————————————
原文链接：https://blog.csdn.net/nirendao/article/details/48863215
"""
