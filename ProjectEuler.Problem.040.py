from ProjectEulerCommon import Answer
from itertools import count

def generate_digit_of_irrational_decimal_fraction():
    for i in count(1):
        for j in str(i):
            yield int(j)

Answer(
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 1) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 10) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 100) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 1000) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 10000) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 100000) *
    next(x for i, x in enumerate(generate_digit_of_irrational_decimal_fraction()) if i + 1 == 1000000)
)
