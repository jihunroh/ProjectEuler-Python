from math import sqrt
from itertools import count

def generate_triangular_number():
    for i in count(1):
        yield int(i* (i + 1) * 0.5)

def generate_pentagonal_number():
    for i in count(1):
        yield int(i* (3 * i - 1) * 0.5)

def is_triangular(n):
   return ((-1 + sqrt(1 + 8 * n)) / 2).is_integer()

def is_pentagonal(n):
    return ((1 + sqrt(1 + 24 * n)) / 6).is_integer()
   
def is_hexagonal(n):
    return ((1 + sqrt(1 + 8 * n)) / 4).is_integer()
