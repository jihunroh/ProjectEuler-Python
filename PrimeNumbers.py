from math import sqrt
from itertools import islice, takewhile, count, chain

def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for divisor in [a for a in range(3, int(sqrt(x)) + 1, 2)]:
        if x % divisor == 0:
            return False
    return True

def generate_prime():
    return filter(lambda n: is_prime(n), chain([2], count(3, 2)))

def generate_prime_below(upperbound):
    return takewhile(lambda x: x <= upperbound, generate_prime())

def generate_prime_above(lowerbound):
    n = lowerbound + 1 if lowerbound % 2 == 0 else lowerbound

    while True:
        if is_prime(n):
            yield n
        n += 2

def generate_prime_in(lowerbound, upperbound):
    n = lowerbound + 1 if lowerbound % 2 == 0 else lowerbound

    while n <= upperbound:
        if is_prime(n):
            yield n
        n += 2

def generate_composite():
    n = 4
    for n in count(4):
        if not is_prime(n):
            yield n
        else:
            continue

def generate_composite_below(upperbound):
    return takewhile(lambda x: x <= upperbound, generate_composite())
