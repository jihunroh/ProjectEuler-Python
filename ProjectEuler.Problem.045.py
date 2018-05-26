from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true
from ProjectEulerCommons.GeometricalNumbers import generate_triangular_number, is_hexagonal, is_pentagonal

Answer(
    first_true(generate_triangular_number(), pred = lambda x: x > 40755 and is_hexagonal(x) and is_pentagonal(x))
)

"""
------------------------------------------------
   ProjectEuler.Problem.045.py
   The Answer is: 1533776805
   Time Elasped: 0.08972334861755371sec
------------------------------------------------
"""
