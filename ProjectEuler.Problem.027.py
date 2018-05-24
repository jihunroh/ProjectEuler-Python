from ProjectEulerCommon import Answer
from ProjectEulerCommon import max_index, product, first_true_index
from PrimeNumbers import is_prime
from itertools import count

def generate_formula_value(a, b):
    for n in count(0):
        yield n**2 + a * n + b

def count_produced_prime_numbers(a, b):
    return first_true_index(generate_formula_value(a, b), pred = lambda enum: not is_prime(enum[1]))

Answer(
    product(max_index({(a, b): count_produced_prime_numbers(a, b)
    for a in range(-1000, 1000 + 1)
    for b in range(-1000, 1000 + 1)})[0])
)
