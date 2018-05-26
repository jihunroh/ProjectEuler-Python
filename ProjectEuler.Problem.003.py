from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Factors import factorize
from ProjectEulerCommons.PrimeNumbers import is_prime

Answer(
    max([x for x in factorize(600851475143) if is_prime(x)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.003.py
   The Answer is: 6857
   Time Elasped: 0.23537230491638184sec
------------------------------------------------
"""
