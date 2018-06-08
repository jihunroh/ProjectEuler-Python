from itertools import count
from fractions import Fraction as fraction
from ProjectEulerCommons.Factors import get_GCD

def generate_digit_of_irrational_decimal_fraction():
    for i in count(1):
        for j in str(i):
            yield int(j)

def get_irreducibe_fraction(fraction):
    GCD = get_GCD([fraction[0], fraction[1]])
    return (int(fraction[0] / GCD), int(fraction[1] / GCD))

