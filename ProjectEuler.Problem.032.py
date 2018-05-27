from ProjectEulerCommons.Base import *
from ProjectEulerCommons.PandigitalNumbers import generate_pandigital_digits_list, generate_pandigital

Answer(
        sum(set([int(str(pandigital)[multiplicand_length + multiplier_length:])
            for pandigital in generate_pandigital()
            for multiplicand_length in range(1, 8)
            for multiplier_length in range(1, 9 - multiplicand_length)
            if int(str(pandigital)[:multiplicand_length]) * int(str(pandigital)[multiplicand_length:multiplicand_length + multiplier_length])
            == int(str(pandigital)[multiplicand_length + multiplier_length:])
        ]))
)

"""
------------------------------------------------
   ProjectEuler.Problem.032.py
   The Answer is: 112740
   Time Elasped: 22.33826231956482sec
------------------------------------------------
"""
