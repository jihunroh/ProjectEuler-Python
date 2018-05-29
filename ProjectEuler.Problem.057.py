from ProjectEulerCommons.Base import *
from fractions import Fraction

def generate_continued_fraction():
    result = 1
    while True:
        result = Fraction(1 + 1 / (1 + result))
        yield result

Answer(
    quantify(take(1000, generate_continued_fraction()), lambda fraction: len(str(fraction.numerator)) > len(str(fraction.denominator)))
)

"""
------------------------------------------------
   ProjectEuler.Problem.057.py
   The Answer is: 153
   Time Elasped: 0.0738372802734375sec
------------------------------------------------
"""
