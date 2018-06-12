from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import is_prime

def generate_formula_value(a, b):
    for n in count(0):
        yield n**2 + a * n + b

def count_produced_prime_numbers(a, b):
    return first_true_index(generate_formula_value(a, b), pred = lambda enum: not is_prime(enum[1]))

Answer(
    prod(max_index({(a, b): count_produced_prime_numbers(a, b)
    for a in range(-1000, 1000 + 1)
    for b in range(-1000, 1000 + 1)})[0])
)

"""
------------------------------------------------
   ProjectEuler.Problem.027.py
   The Answer is: -59231
   Time Elasped: 14.774448156356812sec
------------------------------------------------
"""
