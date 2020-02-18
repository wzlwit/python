from collections import Iterator
isinstance((x for x in range(10)), Iterator)
# True
isinstance([], Iterator)
# False
isinstance({}, Iterator)
# False
isinstance('abc', Iterator)
# False

# *: Generator is an object of Iterator. Though list, str are iterable, but the are not Iterator

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

iter() # convert to an interator.

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640
