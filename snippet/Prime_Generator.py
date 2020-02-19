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
https://stackoverflow.com/questions/60306732/how-a-fiter-works-in-a-generator

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


for prime in primes():
    if prime < 20:
        print(prime)
    else:
        break

```
______
Q ref: https://stackoverflow.com/questions/51055987/python-filter-and-generator

what is the process about this practice,  stuck on the
```python
it = _odd_iter()
it = filter(_not_divisible(n), it)
```
Is it stored value like a list or something?
______

I have to try to answer it here:
Note: Generator stores FUNCTION and STATE of the last iteration (if exist).

Key: each filter fucntion -- _not_divisible(divisor) is ADDed to **it** -- _odd_iter()--, during each iteration (the next one after yield, actually)

###take 9 and 11 as an example:

- in next(it) of primes()
1. _odd_iter() returns 9. 
2. 9 is filtered by _not_divisible(3) and returns false.and then next(_odd_iter) runs
3. 11 is returned and checked by all the previous filter functions: _filter(3), filter(5), filter(7) in sequence. All returns True, then next(it) returns 11 as the new Prime number.

- next iteration of Primes() after the above:
1. function filter(_not_divisible(11)) is created and referenced by the generator Primes()
2. _odd_iter() returns 11+2 = 13
3. 13 is filtered by functions from _not_divisible(3) until not_divisible(11)
4. All filters return True
5. So, 'next(it)' returns 13, which is then yielded as the new Prime Number by the statement 'yield p'

。。。。。。


"""
