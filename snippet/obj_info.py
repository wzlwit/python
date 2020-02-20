""" Type() """
import types
type(123) == type(456)
# True
type(123) == int
# True
type('abc') == type('123')
# True
type('abc') == str
# True
type('abc') == type(123)
# False


""" types """


def fn():
    pass


type(fn) == types.FunctionType
# True
type(abs) == types.BuiltinFunctionType
# True
type(lambda x: x) == types.LambdaType
# True
type((x for x in range(10))) == types.GeneratorType
# True


""" isinstance() """
a = Animal()
d = Dog()
h = Husky()
isinstance(h, Husky)
# True

# one of a sequece of types
isinstance([1, 2, 3], (list, tuple))
# True
isinstance((1, 2, 3), (list, tuple))
# True

""" dir() """
# get all attributes and methods from an object


""" getattr(), setattr(), hasattr() """
# manipulate attributes and status


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

hasattr(obj, 'x')  # 有属性'x'吗？
# True
obj.x
# 9
hasattr(obj, 'y')  # 有属性'y'吗？
# False
setattr(obj, 'y', 19)  # 设置一个属性'y'
hasattr(obj, 'y')  # 有属性'y'吗？
# True
getattr(obj, 'y')  # 获取属性'y'
# 19
obj.y  # 获取属性'y'
# 19

getattr(obj, 'z')  # 获取属性'z'
# Traceback(most recent call last):
#     File "<stdin>", line 1, in < module >
# AttributeError: 'MyObject' object has no attribute 'z'

getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404
# 404

hasattr(obj, 'power')  # 有属性'power'吗？
# True
getattr(obj, 'power')  # 获取属性'power'
# <bound method MyObject.power of < __main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
fn  # fn指向obj.power
# <bound method MyObject.power of < __main__.MyObject object at 0x10077a6a0>>
fn()  # 调用fn()与调用obj.power()是一样的
# 81
