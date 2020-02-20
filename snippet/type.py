""" type() """
# * 1. show type of an object
# * 2. dynamically create a class


def fn(self, name='world'):  # def fn first
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # create Hello class
h = Hello()
h.hello()
# Hello, world.
print(type(Hello))
# <class 'type'>
print(type(h))
# <class '__main__.Hello'>
