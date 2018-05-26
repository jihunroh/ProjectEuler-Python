from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import max_index

def get_triangle_length_pairs(p):
    return sum([True for a in range(1, p - 2) for b in range(a, p - a - 1) if p - a - b > b and a**2 + b**2 == (p - a - b)**2])

Answer(
    max_index([(p, get_triangle_length_pairs(p)) for p in range(3, 1000 + 1)])[0]
)

"""
------------------------------------------------
   ProjectEuler.Problem.039.py
   The Answer is: 840
   Time Elasped: 43.653260707855225sec
------------------------------------------------
"""
