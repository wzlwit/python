"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
"""


def fib(num, temp={}):
    """用递归计算Fibonacci数"""
    if num in (1, 2):
        return 1

    # NOTE: decrease Repeated Calculation
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]
