""" 子列表元素之和的最大/小值。（使用动态规划可以避免二重循环） """
# 说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值
# https://stackoverflow.com/questions/15062844/maximum-sum-sublist


# mine:
def mssl(l, max=True):
    if max:
        m = 'Max'
        def comp(x, y): return x > y    #* first Match
        # def comp(x, y): return x >= y   #* last Match
        
    else:
        m = 'Min'
        def comp(x, y): return x < y        # * find MINIMUM
        # def comp(x, y): return x <= y

    best = cur = l[0]
    curi = starti = 0
    besti = 1
    size = len(l)
    for i in range(1, size):

        """ INFLECTION POINT """
        if comp(cur+i, l[i]):
            cur += l[i]
        else:  # reset start position
            cur, curi = l[i], i

        if comp(cur, best):
            starti, besti, best = curi, i+1, cur

    # return (m, best, [starti, besti],l[starti:besti])
    return {m: best, 'Index': [starti, besti], 'Sub': l[starti:besti]}


# ref:
def ms(items):
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    # print(overall[size-1])
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


def main():
    # L = list(map(int, input().split()))
    L1 = 1, -2, 3, 5, -3, 2, 4, -2, -8, 8, -8, 5, -2, 7, 7, 2, -6, 5
    L2 = -10, -2, -3, -5, -3, -2, -4, -2, -8, -5, -2, -7, -7, -2, -6, -5
    # ms(L1)
    print(mssl(L1, False))
    # ms(L2)
    print(mssl(L2, False))


if __name__ == '__main__':
    main()
