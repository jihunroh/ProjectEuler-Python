import time
from math import sqrt
T0 = time.clock()

def is_integer(a):
    return a % 1 == 0

#def is_triangular(n):
#    return is_integer((-1 + sqrt(1 + 8 * n)) / 2)

def is_pentagonal(n):
    return is_integer((1 + sqrt(1 + 24 * n)) / 6)
   
def is_hexagonal(n):
    return is_integer((1 + sqrt(1 + 8 * n)) / 4)

def hexagonal():
    i = 1
    while True:
        yield i * (2 * i - 1)
        i += 1

def iterate_seq():
    while True:
        for n in hexagonal():
            if is_pentagonal(n):
                yield n
f = iterate_seq()
print(next(f))
print(next(f))
print(next(f))
#1
#40755
#1533776805
#The execution time is 0.112061200221
print('The execution time is', time.clock()-T0)