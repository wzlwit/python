sum = 0
for x in range(101):
    sum += x
print(sum)


# x = int(input('x = '))
# y = int(input('y = '))
x = 24
y = 13
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d and %d gong yue shu: %d' % (x, y, factor))
        print('%d and %d gong bei shu: %d' % (x, y, x * y // factor))
        break

row = int(input('enter lines: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()