from ProjectEulerCommon import Answer
from Factors import factorize
from itertools import count
from GeometricalNumbers import generate_triangular_number

Answer(
    next(x for x in generate_triangular_number() if len(factorize(x)) > 500)
)