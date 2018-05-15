import time
from math import sqrt

T0 = time.clock()
def is_prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        return False
    for divisor in [a for a in range(2, int(sqrt(x)) + 1) if not a % 2 == 0 and not a % 3 == 0 and not a % 5 == 0 and not a % 7 == 0]:
        if x % divisor == 0:
            return False
    return True

def permutations(number):
    number = str(number)
    if len(number) <= 1:
        yield number
    else:
        for perm in permutations(number[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + number[0:1] + perm[i:]
def circulate(number):
    number = str(number)
    if len(number) <= 1:
        yield number
    else:
        for i in range(len(number)):
            yield number[i:] + number[0:i] 

def is_circs_prime(n):
    circs = circulate(n)
    while True:
        try:
            y = int(next(circs))
            if not is_prime(y):
                return False
        except StopIteration:
            break
    return True

Total = [x for x in range(1000000) if is_circs_prime(x)]
print(len(Total))
print('The execution time is', time.clock()-T0)