from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.PrimeNumbers import generate_prime_below
from itertools import takewhile

Answer(
    sum([n for n in generate_prime_below(2000000)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.010.py
   The Answer is: 142913828922
   Time Elasped: 25.362140655517578sec
------------------------------------------------
"""
