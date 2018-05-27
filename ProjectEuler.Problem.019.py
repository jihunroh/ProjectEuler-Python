from ProjectEulerCommons.Base import *
from calendar import monthrange

Answer(
    quantify(
        [(year, month) for year in range(1901, 2000 + 1) for month in range(1, 12 + 1)],
        lambda year_month_pair: monthrange(year_month_pair[0], year_month_pair[1])[0] == 6
    )
)

"""
------------------------------------------------
   ProjectEuler.Problem.019.py
   The Answer is: 171
   Time Elasped: 0.012347698211669922sec
------------------------------------------------
"""
