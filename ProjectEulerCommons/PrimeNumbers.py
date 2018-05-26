from math import sqrt
from itertools import islice, takewhile, count, chain

def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0:
        return False
    if sum(map(int, str(x))) % 3 == 0:
        return False
    for divisor in [a for a in range(5, int(sqrt(x)) + 1, 2)]:
        if x % divisor == 0:
            return False
    return True

def generate_prime():
    return filter(lambda n: is_prime(n), chain([2], count(3, 2)))

def generate_prime_below(upperbound, reverse = False):
    if reverse:
        upperbound = upperbound - 1 if upperbound % 2 == 0 else upperbound
        return filter(is_prime, range(upperbound, 1, - 2))
    else:
        return takewhile(lambda x: x <= upperbound, generate_prime())

def generate_prime_above(lowerbound):
    n = lowerbound + 1 if lowerbound % 2 == 0 else lowerbound
    return filter(lambda n: is_prime(n), count(n, 2))

def generate_prime_in(lowerbound, upperbound):
    n = lowerbound + 1 if lowerbound % 2 == 0 else lowerbound
    return filter(lambda n: is_prime(n) and n <= upperbound, count(n, 2))

def generate_composite():
    return filter(lambda n: not is_prime(n), count(4))

def generate_composite_below(upperbound):
    return takewhile(lambda x: x <= upperbound, generate_composite())
