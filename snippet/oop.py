# * 'feel-like' object

# * METHODS

""" __str__ """  # * for print

""" __repr__ """  # * for developers, when call obj/cls name


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


""" __iter__ """  # used in 'for...in', like List or Tuple


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # instance itself is iterable, so return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # exit iteration
            raise StopIteration()
        return self.a  # return next value
