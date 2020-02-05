# 简介Python之super的用法及原理
# https://blog.csdn.net/nirendao/article/details/48863215

# * MRO: mehtod resolution order

class A(object):
    def __init__(self):
        print("In A's __init__()")


class B(A):
    def __init__(self):
        print("Enter B's __init__()")
        A.__init__(self)
        print("Leave B's __init__()")


class C(A):
    def __init__(self):
        print("Enter C's __init__()")
        A.__init__(self)
        print("Leave C's __init__()")


class D(B, C):
    pass    # *: default constructor is from the closest parent.

# output:
"""
Enter B's __init__()
In A's __init__()
Leave B's __init__()
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""


class E(B, C):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)

d = D()
print()
e = E()
print(d.__class__.__mro__)
