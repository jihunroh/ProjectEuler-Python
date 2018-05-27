from ProjectEulerCommons.Base import *

Answer(
    sum([10 - ceil((10**(digit_length - 1))**(1 / digit_length)) for digit_length in range(1, first_true(count(1), pred = lambda digit_length: ceil((10**(digit_length - 1))**(1 / digit_length)) == 10))])
)

"""
------------------------------------------------
   ProjectEuler.Problem.063.py
   The Answer is: 49
   Time Elasped: 0.005910634994506836sec
------------------------------------------------
"""
