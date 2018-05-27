from ProjectEulerCommons.Base import *

Answer(
    quantify((combination(n, r) for n in range(1, 100 + 1) for r in range(2, n - 1)), pred = lambda x: x > 1000000)
)

"""
------------------------------------------------
   ProjectEuler.Problem.053.py
   The Answer is: 4075
   Time Elasped: 0.05704045295715332sec
------------------------------------------------
"""
