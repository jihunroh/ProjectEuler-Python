from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true
from Factors import factorize
from itertools import count
from GeometricalNumbers import generate_triangular_number

Answer(
    first_true(generate_triangular_number(), None, lambda n: len(factorize(n)) > 500)
)
