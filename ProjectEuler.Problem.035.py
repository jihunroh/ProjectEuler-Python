from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import quantify, first_true, joined_int
from ProjectEulerCommons.PrimeNumbers import generate_prime_below, is_prime
from itertools import islice

def circulations(target_list):
    for i in range(len(target_list)):
        yield target_list[i:] + target_list[:i]

Answer(
    quantify(
        generate_prime_below(1000000),
        lambda prime: first_true(
                        islice(circulations(list(map(int, str(prime)))), 1, None),
                        pred = lambda digitlist: not is_prime(joined_int(digitlist))
                        ) == False
    )
)

"""
------------------------------------------------
   ProjectEuler.Problem.035.py
   The Answer is: 55
   Time Elasped: 12.629229307174683sec
------------------------------------------------
"""
