from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true
from ProjectEulerCommons.PandigitalNumbers import generate_pandigital, is_pandigital
from ProjectEulerCommons.PrimeNumbers import is_prime, generate_prime_below

Answer(
    first_true([first_true(generate_pandigital(range(1, digit + 1), reverse = True), pred = is_prime) for digit in range(9, 0, -1)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.041.py
   The Answer is: 7652413
   Time Elasped: 1.6635828018188477sec
------------------------------------------------
"""
