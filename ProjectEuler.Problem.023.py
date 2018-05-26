from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Factors import factorize

list_abundant = [n for n in range(1, 28123 + 1) if sum(factorize(n)[0:-1]) > n]

Answer(
    sum(set(range(1, 28123 + 1)) - set([a + b for a in list_abundant for b in list_abundant if a <= b and a + b <= 28123]))
)

"""
------------------------------------------------
   ProjectEuler.Problem.023.py
   The Answer is: 4179871
   Time Elasped: 5.314753293991089sec
------------------------------------------------
"""
