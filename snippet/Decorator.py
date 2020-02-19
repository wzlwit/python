def now():
    print('2015-3-25')


f = now
f()
# 2015-3-25

now.__name__
# 'now'
f.__name__
# 'now'


"""
希望增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
"""


def log(func):
    # decorator就是一个返回函数的高阶函数
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
# call now():
# 2015-3-25

# *把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
""" 
# 原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数
"""


# PASS in args for decorator. return a decorator
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
# execute now():
# 2015-3-25

# EQUAL:
now = log('execute')(now)


# __name___, 需要把原始函数的__name__等属性复制到wrapper()函数中，

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator