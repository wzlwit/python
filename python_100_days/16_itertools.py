import itertools
# 排列
p = itertools.permutations('ABCD')
c = itertools.combinations('ABCDE', 3)
x = itertools.product('ABCD', '123')

for v in p:
    print(v)

print()
for v in c:
    print(v)

print()
for v in x:
    print(v)
