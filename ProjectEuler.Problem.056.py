from ProjectEulerCommons.Base import *

Answer(
    max([sum([int(digit) for digit in str(a**b)]) for a in range(100) for b in range(100)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.056.py
   The Answer is: 972
   Time Elasped: 0.2762727737426758sec
------------------------------------------------
"""
