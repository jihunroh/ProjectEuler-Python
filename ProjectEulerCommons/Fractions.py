from itertools import count
from fractions import Fraction as fraction
from ProjectEulerCommons.Factors import get_GCD

def generate_continued_fraction():
    result = 1
    while True:
        result = fraction(1 + 1 / (1 + result))
        yield result

def repeating_decimal(numerator, denominator): # http://codepad.org/hKboFPd2
    prefix, c = [], 10 * (numerator % denominator)
    digits, passed = [], {}

    while c and c < denominator:
        c *= 10
        prefix.append(0)
    for i in count(0):
        if c in passed:
            prefix += digits[:passed[c]]
            return (numerator // denominator, prefix, digits[passed[c]:])
        passed[c] = i
        digits.append(c // denominator)
        c = 10 * (c % denominator)