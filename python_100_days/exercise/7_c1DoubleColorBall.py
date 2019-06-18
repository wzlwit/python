from random import randrange, randint, sample


def display(balls):
    for i, ball in enumerate(balls): #!  two iterators
        if i == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注 (how many tickets): '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
