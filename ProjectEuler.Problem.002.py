from ProjectEulerCommons.Base import *
from ProjectEulerCommons.FibonacciSequence import generate_fibonacci

Answer(
    sum([x for x in generate_fibonacci(4000000) if x % 2 == 0])
)

"""
------------------------------------------------
   ProjectEuler.Problem.002.py
   The Answer is: 4613732
   Time Elasped: 0.01695561408996582sec
------------------------------------------------
"""
