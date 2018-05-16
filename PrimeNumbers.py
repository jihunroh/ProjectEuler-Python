from math import sqrt

def is_prime(x):
    if x % 2 == 0:
        return False
    if x % 3 == 0:
        return False
    if x % 5 == 0:
        return False
    if x % 7 == 0:
        return False
    if x % 11 == 0:
        return False
    if x % 13 == 0:
        return False
    for divisor in [a for a in range(2, int(sqrt(x)) + 1) if not a % 2 == 0 and not a % 3 == 0 and not a % 5 == 0 and not a % 7 == 0]:
        if x % divisor == 0:
            return False
    return True

def iterate_prime():
    n = 2
    yield n
    n = 3
    yield n

    while True:
        n += 2
        if is_prime(n):
            yield n