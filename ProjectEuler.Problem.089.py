from ProjectEulerCommons.Base import *

def shorten_roman(roman):
    shorten_dic = {
        'VIIII': 'IX', #9
        'LXXXX': 'XC', #90
        'DCCCC': 'CM', #900
        'IIII' : 'IV', #4
        'XXXX' : 'XL', #40
        'CCCC' : 'CD'  #400
    }
    for key, value in shorten_dic.items():
        roman = roman.replace(key, value)

    return roman

with open('ProjectEuler.Problem.089.roman.txt', 'r') as f:
    roman_num_list = [line.replace('\n', '') for line in f.readlines()]

Answer(
    sum(map(len, roman_num_list)) - sum(map(len, map(shorten_roman, roman_num_list)))
)

"""
------------------------------------------------
   ProjectEuler.Problem.089.py
   The Answer is: 743
   Time Elasped: 0.014960527420043945sec
------------------------------------------------
"""
