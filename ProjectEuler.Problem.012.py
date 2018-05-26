from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true
from ProjectEulerCommons.Factors import factorize
from itertools import count
from ProjectEulerCommons.GeometricalNumbers import generate_triangular_number

Answer(
    first_true(generate_triangular_number(), pred = lambda n: len(factorize(n)) > 500)
)

"""
------------------------------------------------
   ProjectEuler.Problem.012.py
   The Answer is: 76576500
   Time Elasped: 5.775555849075317sec
------------------------------------------------
"""
