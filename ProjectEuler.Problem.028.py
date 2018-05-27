from ProjectEulerCommons.Base import *

def leftup(n): # 1, 7, 21, 43
    return  4 * n ** 2 - 6 * n + 3

def leftdown(n): # 1, 5, 17, 37
    return  4 * n ** 2 - 8 * n + 5

def rightup(n): # 1, 9, 25, 49
    return  4 * n ** 2 - 4 * n + 1

def rightdown(n): # 1, 3, 13, 31
    return  4 * n ** 2 - 10 * n + 7

Answer(
    1 + sum([sum([leftup(i), leftdown(i), rightup(i), rightdown(i)]) for i in range(2, int(1001 / 2) + 2)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.028.py
   The Answer is: 669171001
   Time Elasped: 0.0069446563720703125sec
------------------------------------------------
"""
