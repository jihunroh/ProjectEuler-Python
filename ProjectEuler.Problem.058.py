from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import is_prime

def generate_prime_diagonal_ratio():
    count_prime = 0
    for layer_n in count(1):
        diagonals = (4 * layer_n**2 - 8 * layer_n + 5, 4 * layer_n**2 - 10 * layer_n + 7, 4 * layer_n**2 - 6 * layer_n + 3, (layer_n + 1)**2) # leftup, rightup, leftdown, rightdown
        count_prime += quantify(diagonals, is_prime)
        yield (layer_n, count_prime / (4 * layer_n - 3))

Answer(
    first_true(islice(generate_prime_diagonal_ratio(), 1, None), pred = lambda x: x[1] < 0.1)[0] * 2 - 1
)

"""
------------------------------------------------
   ProjectEuler.Problem.058.py
   The Answer is: 26241
   Time Elasped: 3.9683940410614014sec
------------------------------------------------
"""
