from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import first_true_index
from ProjectEulerCommons.FibonacciSequence import generate_fibonacci

Answer(
    first_true_index(generate_fibonacci(), pred = lambda enum: len(str(enum[1])) == 1000) + 1
)

"""
------------------------------------------------
   ProjectEuler.Problem.025.py
   The Answer is: 4782
   Time Elasped: 0.07437849044799805sec
------------------------------------------------
"""
