from ProjectEulerCommons.Base import *
from ProjectEulerCommons.Fractions import generate_digit_of_irrational_decimal_fraction

Answer(
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 10) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 100) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 10000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 100000) *
    first_true_value(generate_digit_of_irrational_decimal_fraction(), pred = lambda enum: enum[0] + 1 == 1000000)
)

"""
------------------------------------------------
   ProjectEuler.Problem.040.py
   The Answer is: 210
   Time Elasped: 0.7999002933502197sec
------------------------------------------------
"""
