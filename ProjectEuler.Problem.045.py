from ProjectEulerCommons.Base import *
from ProjectEulerCommons.GeometricalNumbers import generate_triangular, is_hexagonal, is_pentagonal

Answer(
    first_true(generate_triangular(), pred = lambda x: x > 40755 and is_hexagonal(x) and is_pentagonal(x))
)

"""
------------------------------------------------
   ProjectEuler.Problem.045.py
   The Answer is: 1533776805
   Time Elasped: 0.08972334861755371sec
------------------------------------------------
"""
