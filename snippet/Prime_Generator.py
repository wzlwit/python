def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # initialize
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # the filter is added into 'it' generator during each next()


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

iter = _odd_iter()
test = filter(_not_divisible(3), iter)

for _ in range(100):
    print(next(test))
