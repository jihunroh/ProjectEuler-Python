from ProjectEulerCommons.Base import Answer, first_true
from ProjectEulerCommons.Factors import factorize
from ProjectEulerCommons.GeometricalNumbers import generate_triangular

Answer(
    first_true(generate_triangular(), pred = lambda n: len(factorize(n)) > 500)
)

"""
------------------------------------------------
   ProjectEuler.Problem.012.py
   The Answer is: 76576500
   Time Elasped: 5.775555849075317sec
------------------------------------------------
"""
