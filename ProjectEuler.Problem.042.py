from ProjectEulerCommons.Base import *
from ProjectEulerCommons.GeometricalNumbers import is_triangular
from string import ascii_uppercase

def is_triangle_word(word):
    word_value = sum(map(lambda x: ascii_uppercase.index(x) + 1, word))
    return is_triangular(word_value)

with open('ProjectEuler.Problem.042.words.txt', 'r') as f:
    words = [line.replace('"', '').split(',') for line in f.readlines()][0]

Answer(
    quantify(words, is_triangle_word)
)

"""
------------------------------------------------
   ProjectEuler.Problem.042.py
   The Answer is: 162
   Time Elasped: 0.012920379638671875sec
------------------------------------------------

"""
