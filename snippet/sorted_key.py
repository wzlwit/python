sorted([36, 5, -12, 9, -21], key=abs)
# [5, 9, -12, -21, 36]

""" 
keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
"""

sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']
""" 符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面 """

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']

# TODO: reverse
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']