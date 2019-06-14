# https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/07.%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%92%8C%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md

import sys
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
# :: indicate step
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格的拷贝
print(str3.strip())


# list
list1 = [1, 3, 5, 7, 100]
list2 = ['hello']*5

list1.append(200)
list1.insert(1, 400)
list1 += [1000, 2000]
print(list1)
print(len(list1))
#remove element
list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
del list1[0]
print(list1)
# clear a list
list1.clear()


f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# yield
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a