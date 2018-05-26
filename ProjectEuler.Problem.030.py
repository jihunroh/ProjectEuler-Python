from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true
from itertools import count

Answer(
    sum([n for n in range(1, 9**5 * first_true(count(1), pred = lambda m: 10**(m - 1) > 9**5 * m) - 1) if n == sum([int(digit)**5 for digit in str(n)])]) - 1
)

"""
------------------------------------------------
   ProjectEuler.Problem.030.py
   The Answer is: 443839
   Time Elasped: 1.824345350265503sec
--------------------------------------------
"""
