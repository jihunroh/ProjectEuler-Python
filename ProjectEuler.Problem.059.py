from ProjectEulerCommons.Base import *
from string import ascii_lowercase

with open('ProjectEuler.Problem.059.cipher.txt', 'r') as f:
    ascii_list = [list(map(int, line.split(','))) for line in f.readlines()][0]

Answer(
    sum(map(ord, first_true((''.join([chr(ascii^key[i % 3]) for i, ascii in enumerate(ascii_list)]) for key in ((ord(key1), ord(key2), ord(key3)) for key1 in ascii_lowercase for key2 in ascii_lowercase for key3 in ascii_lowercase)), pred = lambda x: ' the ' in x)))
)

"""
------------------------------------------------
   ProjectEuler.Problem.059.py
   The Answer is: 107359
   Time Elasped: 1.8331317901611328sec
------------------------------------------------
"""
