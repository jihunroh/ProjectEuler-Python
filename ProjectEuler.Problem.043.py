from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PandigitalNumbers import generate_pandigital

Answer(
    sum([num for num in generate_pandigital(range(0, 10))
    if int(str(num)[1:4]) % 2 == 0 and
    int(str(num)[2:5]) % 3 == 0 and
    int(str(num)[3:6]) % 5 == 0 and
    int(str(num)[4:7]) % 7 == 0 and
    int(str(num)[5:8]) % 11 == 0 and
    int(str(num)[6:9]) % 13 == 0 and
    int(str(num)[7:10]) % 17 == 0])
)

"""
------------------------------------------------
   ProjectEuler.Problem.043.py
   The Answer is: 16695334890
   Time Elasped: 20.61912775039673sec
------------------------------------------------
"""
