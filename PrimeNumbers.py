from math import sqrt
from itertools import islice

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for divisor in [a for a in range(3, int(sqrt(x)) + 1, 2)]:
        if x % divisor == 0:
            return False
    return True

def generate_prime():
    n = 2
    yield n
    n = 3
    yield n
    
    while True:
        n += 2
        if is_prime(n):
            yield n

def get_nth_prime(n):
    f = generate_prime()
    return list(islice(f, n))[-1]
