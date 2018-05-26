from ProjectEulerCommons.Base import Answer

Answer(
    sum(range(1, 100 + 1)) ** 2  - sum([x * x for x in range(1, 100 + 1)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.006.py
   The Answer is: 25164150
   Time Elasped: 0.004987478256225586sec
------------------------------------------------
"""
