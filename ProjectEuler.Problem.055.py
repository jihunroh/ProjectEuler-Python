from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PalindromicNumbers import is_palindromic

def is_Lychrel_number(n):
    num_processed = n
    for count_process in range(1, 50):
        num_processed = num_processed + int(''.join(reversed(str(num_processed))))
        if is_palindromic(num_processed):
            return False
    return True

Answer(
    quantify(range(10000 + 1), is_Lychrel_number)
)

"""
------------------------------------------------
   ProjectEuler.Problem.055.py
   The Answer is: 249
   Time Elasped: 0.10667896270751953sec
------------------------------------------------
"""
