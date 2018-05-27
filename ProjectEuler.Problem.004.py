from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PalindromicNumbers import is_palindromic

Answer(
    max([x * y  for x in range(100,1000) for y in range(100,1000) if is_palindromic(x * y)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.004.py
   The Answer is: 906609
   Time Elasped: 1.059168815612793sec
------------------------------------------------
"""
