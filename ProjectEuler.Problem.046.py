from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import generate_composite, generate_prime_below
from math import sqrt

def is_goldbach_conjecture(num):
    return True if next((prime for prime in generate_prime_below(num - 2) if sqrt(0.5 * (num - prime)).is_integer()), False) != False else False

Answer(
    first_true(generate_composite(), pred = lambda n: not n % 2 == 0 and not is_goldbach_conjecture(n))
)

"""
------------------------------------------------
   ProjectEuler.Problem.046.py
   The Answer is: 5777
   Time Elasped: 1.0392160415649414sec
------------------------------------------------
"""
