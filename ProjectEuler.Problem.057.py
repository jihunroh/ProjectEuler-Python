from ProjectEulerCommons.Base import *
from ProjectEulerCommons.Fractions import generate_continued_fraction

Answer(
    quantify(take(1000, generate_continued_fraction()), lambda frac: len(str(frac.numerator)) > len(str(frac.denominator)))
)

"""
------------------------------------------------
   ProjectEuler.Problem.057.py
   The Answer is: 153
   Time Elasped: 0.0738372802734375sec
------------------------------------------------
"""
