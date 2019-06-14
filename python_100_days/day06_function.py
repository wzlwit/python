from random import randint


def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
