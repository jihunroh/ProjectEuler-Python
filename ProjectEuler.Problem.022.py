from ProjectEulerCommons.Base import Answer
from string import ascii_uppercase
from string import ascii_uppercase

with open('ProjectEuler.Problem.022.names.txt', 'r') as f:
    names = sorted([line.replace('"', '').split(',') for line in f.readlines()][0])

Answer(
    sum([(i + 1) * sum([ascii_uppercase.index(alphabet) + 1 for alphabet in name]) for i, name in enumerate(names)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.022.py
   The Answer is: 871198282
   Time Elasped: 0.020864486694335938sec
------------------------------------------------
"""
