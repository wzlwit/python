# 偏函数， freeze some parameters
import functools
int2 = functools.partial(int, base=2)
int2('1000000')
# 64
int2('1010101')
# 85

# example:
max2 = functools.partial(max, 10)

max2(5, 6, 7)   
"""
args = (10, 5, 6, 7)
max(*args)
"""
# output: 10