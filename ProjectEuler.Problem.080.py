from ProjectEulerCommons.Base import *
from decimal import Decimal, getcontext

getcontext().prec = 102

Answer(
    sum(sum(digits_list(int(Decimal(n).sqrt() * 10**100))[:100]) for n in range(1, 101) if not sqrt(n).is_integer())
)

"""
------------------------------------------------
   ProjectEuler.Problem.080.py
   The Answer is: 40886
   Time Elasped: 0.03291463851928711sec
------------------------------------------------
"""
