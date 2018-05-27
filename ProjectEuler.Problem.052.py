from ProjectEulerCommons.Base import *

Answer(
    next(first_true(range(10 ** (digit - 1), int(10 ** digit / 6)), pred = lambda num: all_equal(map(sorted, map(str, [num, num * 2, num * 3, num * 4, num * 5, num * 6])))) 
    for digit in count(2) if first_true(range(10 ** (digit - 1), int(10 ** digit / 6)), pred = lambda num: all_equal(map(sorted, map(str, [num, num * 2, num * 3, num * 4, num * 5, num * 6])))) != False)
)

"""
------------------------------------------------
   ProjectEuler.Problem.052.py
   The Answer is: 142857
   Time Elasped: 0.8858544826507568sec
------------------------------------------------
"""
