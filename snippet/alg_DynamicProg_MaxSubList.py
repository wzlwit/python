""" 子列表元素之和的最大值。（使用动态规划可以避免二重循环） """
# 说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值
# https://stackoverflow.com/questions/15062844/maximum-sum-sublist


def mssl(l):
    best = cur = 0
    curi = starti = besti = 0
    for ind, i in enumerate(l):
        if cur+i > 0:
            cur += i
        else:  # reset start position
            cur, curi = 0, ind+1

        if cur > best:
            starti, besti, best = curi, ind+1, cur
    return starti, besti, best


def ms(items):
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    print(overall[size-1])
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


def main():
    # L = list(map(int, input().split()))
    L1 = 1, -2, 3, 5, -3, 2, 4, -2, -8, 5, -2, 7, 7, 2, -6, 5
    L2 = -1, -2, -3, -5, -3, -2, -4, -2, -8, -5, -2, -7, -7, -2, -6, -5
    ms(L2)
    print(mssl(L1))


if __name__ == '__main__':
    main()
