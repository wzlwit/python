""" __getitem__ """


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


# iterator can not be accessed by index, so:

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
f[0]
# 1
f[1]
# 1
f[2]
# 2
f[3]
# 3
f[10]
# 89
f[100]
# 573147844013817084101


# TODO:  pass in a SLICE

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
f[0:5]
# [1, 1, 2, 3, 5]
f[:10]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


""" chained call """  # for dynamic call


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# * 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
Chain().status.user.timeline.list
# '/status/user/timeline/list'
