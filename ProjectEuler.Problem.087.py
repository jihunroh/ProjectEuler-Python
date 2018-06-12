from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import generate_prime_below

Answer(
    len(
        set([a**2 + b**3 + c**4
            for c in generate_prime_below(int((50000000 - 12)**0.25) + 1)
            for b in generate_prime_below(int((50000000 - c)**(1/3)) + 1)
            for a in generate_prime_below(int((50000000 - b - c)**0.5) + 1)
            if a**2 + b**3 + c**4 <= 50000000
        ])
    )
)

"""
------------------------------------------------
   ProjectEuler.Problem.087.py
   The Answer is: 1097343
   Time Elasped: 8.729656219482422sec
------------------------------------------------
"""
