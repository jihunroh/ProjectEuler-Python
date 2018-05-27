from ProjectEulerCommons.Base import *

def last_digits_pow(x, y):
    i, result = 1, 1
    while i != y:
        result = int(str(result * x)[-10:])
        i += 1
    return result

Answer(
    str(28433 * last_digits_pow(2, 7830457) + 1)[-10:]
)

"""
------------------------------------------------
   ProjectEuler.Problem.097.py
   The Answer is: 9369996289
   Time Elasped: 7.141899585723877sec
------------------------------------------------
"""
