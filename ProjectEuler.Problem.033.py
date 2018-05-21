from ProjectEulerCommon import Answer
from ProjectEulerCommon import product
from Factors import get_irreducibe_fraction

Answer(
    get_irreducibe_fraction(
    [product(bulator) for bulator in list(zip(*[[numerator, denominator] for numerator in range(10, 100) for denominator in range(10, 100)
    if numerator < denominator and
    ((denominator * int(str(numerator)[1]) == numerator * int(str(denominator)[0]) and str(denominator)[1] == str(numerator)[0]) or
    (denominator * int(str(numerator)[0]) == numerator * int(str(denominator)[1]) and str(denominator)[0] == str(numerator)[1]))]))]
    )[1]
)
