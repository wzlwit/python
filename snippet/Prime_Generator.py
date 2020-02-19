n = 1


def _odd_iter():
    global n
    while True:
            n = n + 2
            yield n


def _not_divisible(d):
    return lambda x: x % d > 0


def primes():
    yield 2
    it = _odd_iter()  # initialize
    while True:
        p = next(it)
        yield p
        it = filter(_not_divisible(p), it)
        # the filter function: _not_divisible(d) is added to the generator(_odd_iter) during each iteration (next one, actually)


for prime in primes():
    if prime < 20:
        print(prime)
    else:
        break

iter = _odd_iter()
test = filter(_not_divisible(3), iter)

for _ in range(20):
    print(next(test))


""" 

Note: Generator stores FUNCTION and STATE of last iteration (if exist).

Key: the filter -- _not_divisible(divisor) is ADDed to **it** (_odd_iter()) during each iteration (the next one after yield, actually)

###take 9 and 11 as an example:

- in next(it) of primes()
1. _odd_iter() returns 9. 
2. 9 is filtered by _not_divisible(3) and returns false.and then next(_odd_iter) runs
3. 11 is returned and checked _filter(3), filter(5), filter(7) in sequence. All is true, then next(it) returns 11 as the new Prime number.

- next iteration of Primes() after the above:
1. filter(_not_divisible(11)) is added to the generator
2. _odd_iter() returns 11+2 = 13
3. 13 is filtered from filter(3) until filter(11), True is returned
4. As all filters returns True, next(it) returns 13, which is yeilded by the statement (yield n)

。。。。。。

I rewrite the code to make it more clear, and it can be visualized in http://www.pythontutor.com/visualize.html#mode=edit
(Pay attention to 9 and 11, step by step)
```Python
n = 1

def _odd_iter():
    global n
    while True:
            n = n + 2
            yield n


def _not_divisible(d):
    return lambda x: x % d > 0


def primes():
    yield 2
    it = _odd_iter()  # initialize
    while True:
        p = next(it)
        yield p
        it = filter(_not_divisible(p), it)
        # the filter function: _not_divisible(d) is added to generator(_odd_iter) during each iteration (next one, actually)


for prime in primes():
    if prime < 20:
        print(prime)
    else:
        break

```




 """
