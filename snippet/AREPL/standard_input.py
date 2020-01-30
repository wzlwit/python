# 3 WAYS:


def standard_input():
    yield 'hello'
    yield 'world'


standard_input = ["hello", "world"]

standard_input = "hello\nworld"

print(input())  # prints hello
print(input())  # prints world

# print(input()) # there is no more input - StopIteration error would be raised
