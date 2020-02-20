# optional way to access inexist attribute
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


""" If attr is not exist, will be serached by __getattr__() """
s = Student()
s.name
# 'Michael'
s.score
# 99


""" return a function """


class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


s.age()
# 25
