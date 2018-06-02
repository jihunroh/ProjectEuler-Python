from ProjectEulerCommons.Base import *
from math import log

with open('ProjectEuler.Problem.099.base_exp.txt', 'r') as f:
    base_exp_pair = [list(map(int, line.replace('\n', '').split(','))) for line in f.readlines()]

Answer(
    max_index(list(enumerate(list(map(lambda x: x[1] * log(x[0]), base_exp_pair)))))[0] + 1
)

"""
------------------------------------------------
   ProjectEuler.Problem.099.py
   The Answer is: 709
   Time Elasped: 0.007979393005371094sec
------------------------------------------------
"""
