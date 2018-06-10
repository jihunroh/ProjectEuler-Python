from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import generate_prime_below

Answer(
    first_true(
        count(3),
        pred = lambda n: count_summation_way(n, list(generate_prime_below(n))) > 5000
    )
)

"""
------------------------------------------------
   ProjectEuler.Problem.077.py
   The Answer is: 71
   Time Elasped: 21.888498544692993sec
------------------------------------------------
"""
