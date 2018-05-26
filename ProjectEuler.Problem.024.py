from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true_value
from itertools import permutations

Answer(
    int(''.join(map(str, first_true_value(permutations(list(range(10))), pred = lambda enum: enum[0] == 1000000 - 1))))
)
"""
------------------------------------------------
   ProjectEuler.Problem.024.py
   The Answer is: 2783915460
   Time Elasped: 1.132969617843628sec
------------------------------------------------
"""
