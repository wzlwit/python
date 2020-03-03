import os
print(os.name)  # operation system
# 'posix': Linux, Unix, Mac OS X
# 'nt': Windows

# os.uname()  # not available in windows

os.environ

os.environ.get('PATH')
# like getattr(), assign a default value if cannot find

os.environ.get('x', 'default')

print(os.path.abspath('.'))  # current absolute path

os.path.join('/Users/michael', 'testdir')

# os.mkdir('/Users/michael/testdir')

os.path.split('/Users/michael/testdir/file.txt')
# split into 2 parts. last part is the last level of path
""" ('/Users/michael/testdir', 'file.txt') """

os.path.splitext('/path/to/file.txt')
# get extension

os.rename('test.txt', 'test.py')

os.remove('test.py')


[x for x in os.listdir('.') if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']