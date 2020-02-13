import math


def is_prime(n):

    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


""" FORMULA """
#  if ((n-1)!+1) % n ==0, then n is prime