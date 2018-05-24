from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true_value
from itertools import count

def generate_digit_of_irrational_decimal_fraction():
    for i in count(1):
        for j in str(i):
            yield int(j)

Answer(
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 10) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 100) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 10000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 100000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1000000)
)
