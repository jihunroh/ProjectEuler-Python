from ProjectEulerCommons.Base import *
from ProjectEulerCommons.Fractions import fraction

Answer(
    prod([fraction(numerator, denominator)
    for numerator in range(10, 100) for denominator in range(numerator + 1, 100)
    if (
        (
            str(denominator)[1] == str(numerator)[0]
            and denominator * int(str(numerator)[1]) == numerator * int(str(denominator)[0])
        )
        or
        (
            str(denominator)[0] == str(numerator)[1]
            and denominator * int(str(numerator)[0]) == numerator * int(str(denominator)[1])
        )
       )
       ]).denominator
)

"""
------------------------------------------------
   ProjectEuler.Problem.033.py
   The Answer is: 100
   Time Elasped: 0.016954898834228516sec
------------------------------------------------
"""
