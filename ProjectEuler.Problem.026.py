from ProjectEulerCommons.Base import *

def generate_recurring_denominator(): #9 > 90 > 99 > 900 > 990 > 999 > 9000 > 9900 > 9990 > 9999 > ...
    for length in count(1):
        for nine_length in range(1, length):
            yield int('9' * nine_length + '0' * (length - nine_length))

def recurring_cycle_length(n):
    denominator = first_true(generate_recurring_denominator(), None, lambda x: x % n == 0)
    return 0 if sum([int(digit) for digit in str(int(denominator // n))]) == 9 else str(denominator).count('9')

Answer(
    max_index({num: recurring_cycle_length(num) for i, num in enumerate(range(1, 1000))})[0]
)

"""
------------------------------------------------
   ProjectEuler.Problem.026.py
   The Answer is: 983
   Time Elasped: 109.18378067016602sec
------------------------------------------------
"""
