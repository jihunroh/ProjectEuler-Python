from ProjectEulerCommons.Base import *
from operator import sub

Answer(
    len([
        [coord1, coord2]
        for coord1 in product(range(50 + 1), range(50 + 1))
        for coord2 in product(range(coord1[0] + 1), range(coord1[1], 50 + 1))
        if coord1 != coord2 and coord1 != (0, 0) and coord2 != (0, 0) and
           (dotproduct(coord1, coord2) == 0 or dotproduct(coord1, list(map(sub, coord1, coord2))) == 0 or dotproduct(coord2, list(map(sub, coord1, coord2))) == 0)
    ])
)

"""
------------------------------------------------
   ProjectEuler.Problem.091.py
   The Answer is: 14234
   Time Elasped: 9.034871816635132sec
------------------------------------------------
"""
