from ProjectEulerCommons.Base import Answer

Answer(
    len(sorted(set([a**b for a in range(2, 100 + 1) for b in range(2, 100 + 1)])))
)

"""
------------------------------------------------
   ProjectEuler.Problem.029.py
   The Answer is: 9183
   Time Elasped: 0.018923044204711914sec
------------------------------------------------
"""
