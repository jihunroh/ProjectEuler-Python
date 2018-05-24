from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true
from GeometricalNumbers import generate_triangular_number, is_hexagonal, is_pentagonal

Answer(
    first_true(generate_triangular_number(), pred = lambda x: x > 40755 and is_hexagonal(x) and is_pentagonal(x))
)
