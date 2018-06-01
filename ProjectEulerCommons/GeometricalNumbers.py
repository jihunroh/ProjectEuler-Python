from math import sqrt
from itertools import count

def generate_triangular():
    for i in count(1):
        yield int(i* (i + 1) * 0.5)

def generate_pentagonal():
    for i in count(1):
        yield int(i* (3 * i - 1) * 0.5)

def is_triangular(n):
   return ((-1 + sqrt(1 + 8 * n)) / 2).is_integer()

def is_pentagonal(n):
    return ((1 + sqrt(1 + 24 * n)) / 6).is_integer()
   
def is_hexagonal(n):
    return ((1 + sqrt(1 + 8 * n)) / 4).is_integer()

def is_heptagonal(n):
    return ((3 + sqrt(9 + 40 * n)) / 10).is_integer()

def is_octagonal(n):
    return ((1 + sqrt(1 + 6 * n)) / 3).is_integer()

def is_square(n):
    return sqrt(n).is_integer()
