def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字 (the name of module being executed)
# 只有被Python解释器直接执行的模块的名字才是__main__ (like main() in Java)
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()