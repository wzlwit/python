""" __slots__ """
# to restrict attributes that can be bind for an instance


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99  # 绑定属性'score'

# Traceback(most recent call last):
#     File "<stdin>", line 1, in < module >
# AttributeError: 'Student' object has no attribute 'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


# !!!: __slots__定义的属性对继承的子类也起作用：


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999

print(g.score)
