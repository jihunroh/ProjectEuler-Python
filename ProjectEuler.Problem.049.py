from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import is_prime

Answer(
    nth((''.join(map(str, [n, n + d, n + 2 * d])) for n in range(1487 + 2, 10000, 2) for d in range(2, int((10000 - n) * 0.5), 2) if is_prime(n) and is_prime(n + d) and is_prime(n + 2 * d) and sorted(str(n)) == sorted(str(n + d)) == sorted(str(n + 2 * d))), 0)
)

"""
------------------------------------------------
   ProjectEuler.Problem.049.py
   The Answer is: 296962999629
   Time Elasped: 8.519287586212158sec
------------------------------------------------
"""
