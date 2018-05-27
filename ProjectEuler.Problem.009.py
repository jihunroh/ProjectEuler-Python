from ProjectEulerCommons.Base import *

Answer(
    product(first_true([(a, b, 1000 - a - b) for a in range(1, 1000) for b in range(a, 1000)], pred = lambda ab_pair: ab_pair[0] * ab_pair[0] + ab_pair[1] * ab_pair[1] == ab_pair[2] * ab_pair[2]))
)

"""
------------------------------------------------
   ProjectEuler.Problem.009.py
   The Answer is: 31875000
   Time Elasped: 0.215423583984375sec
------------------------------------------------
"""
