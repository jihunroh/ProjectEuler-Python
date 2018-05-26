from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.PalindromicNumbers import is_palindromic

Answer(
    sum([num for num in range(1000000) if is_palindromic(num) and is_palindromic(bin(num)[2:])])
)

"""
------------------------------------------------
   ProjectEuler.Problem.036.py
   The Answer is: 872187
   Time Elasped: 0.962346076965332sec
------------------------------------------------
"""
