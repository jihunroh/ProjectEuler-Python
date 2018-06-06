from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PrimeNumbers import generate_prime_below, is_prime

def generate_sum_of_primes(upperbound):
    primes_below = list(generate_prime_below(upperbound))
    primes_below = primes_below[:first_true(count(0), pred = lambda i: sum(primes_below[i:i+13]) > upperbound) + 13]
    len_primes_below = len(primes_below)
    for i in range(len_primes_below  - 1): # i: start_index
        end_index_start = i + 15 if i != 0 else i + 14
        for j in range(end_index_start, len_primes_below , 2):
            sum_primes = sum(primes_below[i:j])
            if sum_primes < upperbound and is_prime(sum_primes):
                yield (sum_primes, j - i)

Answer(
    max_index(list(generate_sum_of_primes(1000000)))[0]
)
#  41 for [2,  3, + 5 + 7 + 11 + 13
# 953 for [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

"""
------------------------------------------------
   ProjectEuler.Problem.050.py
   The Answer is: 997651
   Time Elasped: 700.0637621879578sec
------------------------------------------------
"""
