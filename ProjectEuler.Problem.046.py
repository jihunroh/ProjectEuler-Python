import time
from eulerlibs import is_prime, iterate_prime, is_int
from math import sqrt
T0 = time.clock()
# p + 2 * x ** 2

def is_odd_composite_number(n):
    return not is_prime(n)
def iterate_odd_composite_number():
    n = 3
    while True:
        if is_odd_composite_number(n):
            yield n
        n += 2

def is_goldbach(n):
    f = iterate_prime()
    prime = next(f)

    while ( prime < n):
        if is_int(sqrt((n - prime) / 2)):
            return True 
        prime = next(f)
    return False

g = iterate_odd_composite_number()
while True:
    next_comp = next(g)
    if not is_goldbach(next_comp):
        print(next_comp)
        break

print('The execution time is', time.clock()-T0)