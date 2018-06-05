from ProjectEulerCommons.Base import *
from ProjectEulerCommons.GeometricalNumbers import pentagonal, is_pentagonal

Answer(
    diff(first_true(
        (
            (pentagonal(k), pentagonal(j))
            for k, j in ((k, j) for subrange in count(0, 100) for (k, j) in ((k, j) for k, j in sorted([(k, j) for k in range(subrange, subrange + 100) for j in range(1, k)], key = lambda x: (x[0] - x[1]) * (3 * x[0] + 3 * x[1] - 1))))
        ),
        pred = lambda x: is_pentagonal(x[0] + x[1]) and is_pentagonal(x[0] - x[1])
    ))
)

"""
------------------------------------------------
   ProjectEuler.Problem.044.py
   The Answer is: 5482660
   Time Elasped: 7.399751663208008sec
------------------------------------------------
"""
