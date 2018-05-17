from ProjectEulerCommon import Answer
from Factors import factorize
from itertools import count

def generate_triangular_number():
    for i in count(1):
        yield int(i* (i+1) * 0.5)

Answer(
    next(x for x in generate_triangular_number() if len(factorize(x)) > 500)
)