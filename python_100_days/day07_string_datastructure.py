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
print(str2[-3:-1])  # ! 45 (end exclusive)

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

#* literal representation of Str
print( repr('small')) #! quote included
print(eval("'small'")) #! seems 'small' are typed into the INTERPRETER
print(str("small"))
print("'small'")
print('"small"')
print('\tsmall')
print("\tsmall")

# list
list1 = [1, 3, 5, 7, 100]
list2 = ['hello']*5

list1.append(200)
list1.insert(1, 400)
list1 += [1000, 2000]
list1 += [3000]  # ? only operatable with LIST
print('list1: ', list1)
print('Length of List1: ', len(list1))
# remove element
print('Remove(3): ', list1.remove(3))
if 1234 in list1:
    list1.remove(1234)
del list1[0]
print('List1: ', list1)
# clear a list
list1.clear()


# * using range to create a list
f = [x for x in range(1, 10)]
print(f)
# ? like table multiplication /Cross Join
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# yield

del f[0]

f = range(1, 10)    #Just create a range
print(f)

for x in f:
    print(x)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


# * tuple
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
#! 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
#! tuple not changable

# * set
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
set2 = set(range(1, 10))
print(set2)
set1.add(4)
set1.add(5)
set2.update([11, 12])  # add elements of an array to the set
print(set1)
print(set2)
set2.discard(5)
if 4 in set2:  # ! in
    set2.remove(4)
print(set2)

for elem in set2:
    print(elem ** 2, end=' ')
print()

set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop())
print(set3)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))


# * dictionary (key: valure pair)
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)
