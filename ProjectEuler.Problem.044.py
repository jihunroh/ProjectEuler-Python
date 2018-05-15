import time
from eulerlibs import is_int
T0 = time.clock()

def iterate_pentagonal_number():
    n = 1
    while True:
        yield n * (3 * n - 1) /2
        n += 1
def is_pentagonal(n):
    return is_int((1 + sqrt(1 + 24 * n)) / 6)

print('The execution time is', time.clock()-T0)