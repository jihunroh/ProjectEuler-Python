from math import sqrt
from itertools import islice, takewhile, count, chain, compress

def is_prime(x): # simple 6k ± 1 optimization
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate_6k():
    k = 1
    while True:
        yield 6 * k + 1
        yield 6 * k + 5
        k += 1

def generate_prime():
    return filter(lambda n: is_prime(n), chain([2, 3, 5], generate_prime_candidate_6k()))

# def generate_prime_below(upperbound, reverse = False):
#     if reverse:
#         upperbound = upperbound - 1 if upperbound % 2 == 0 else upperbound
#         return filter(is_prime, range(upperbound, 1, - 2))
#     else:
#         return takewhile(lambda x: x <= upperbound, generate_prime())

def generate_prime_below(upperbound): #https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (upperbound // 2+1)
    for i in range(1, int(upperbound**0.5) // 2+1):
        if sieve[i]:
            sieve[2 * i * (i + 1)::2 * i + 1] = bytearray((upperbound // 2 - 2 * i * (i + 1)) // (2 * i + 1) + 1)
    return iter([2, *compress(range(3, upperbound, 2), sieve[1:])])

def generate_prime_above(lowerbound):
    lowerbound = lowerbound + 1 if lowerbound % 2 == 0 else lowerbound
    return filter(lambda n: is_prime(n), count(lowerbound, 2))

def generate_prime_in(lowerbound, upperbound):
    return takewhile(lambda n: n <= upperbound, generate_prime_above(lowerbound))

def generate_composite():
    return filter(lambda n: not is_prime(n), count(4))

def generate_composite_below(upperbound):
    return takewhile(lambda x: x <= upperbound, generate_composite())
