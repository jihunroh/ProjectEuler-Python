from ProjectEulerCommons.Base import *
from ProjectEulerCommons.Factors import prime_factorize

num = 3
while True:
    if len(prime_factorize(num)) == 4:
        if len(prime_factorize(num + 1)) == 4:
            if len(prime_factorize(num + 2)) == 4:
                if len(prime_factorize(num + 3)) == 4:
                    break
                else:
                    num += 4
            else:
                num += 3
        else:
            num += 2
    else:
        num += 1
Answer(
    num
)

"""
------------------------------------------------
   ProjectEuler.Problem.047.py
   The Answer is: 134043
   Time Elasped: 109.54404807090759sec
------------------------------------------------
"""
