from ProjectEulerCommon import Answer
from GeometricalNumbers import generate_triangular_number, is_hexagonal, is_pentagonal

Answer(
    next(x for x in generate_triangular_number() if x > 40755 and is_hexagonal(x) and is_pentagonal(x))
)
