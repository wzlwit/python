# instance.method() to call method of an instance
""" call instance itself """


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self): # can put in parameters
        print('My name is %s.' % self.name)


s = Student('Michael')
s()
# My name is Michael.


""" Callable """
callable(Student())
# True
callable(max)
# True
callable([1, 2, 3])
# False
callable(None)
# False
callable('str')
# False