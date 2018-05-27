from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import generate_prime, is_prime

def is_truncatable_prime(n):
    if n in [2, 3, 5, 7]:
        return False
    numberlist = [int(str(n)[i:]) for i in range(1, len(str(n)))] + [int(str(n)[:j]) for j in range(1, len(str(n)))]
    for n in numberlist:
        if not is_prime(n):
            return False
    return True

Answer(
    sum([num for num in islice(filter(is_truncatable_prime, generate_prime()), 11)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.037.py
   The Answer is: 748317
   Time Elasped: 7.705394268035889sec
------------------------------------------------
"""
