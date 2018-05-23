from ProjectEulerCommon import Answer
from string import ascii_uppercase
from math import sqrt

def is_triangle_word(word):
    word_value =  sum(list(map(lambda x: ascii_uppercase.index(x) + 1, word)))
    return ((-1 + sqrt(1 + 8 * word_value)) * 0.5).is_integer()

with open('ProjectEuler.Problem.042.words.txt', 'r') as f:
    words = [line.replace('"', '').split(',') for line in f.readlines()][0]

Answer(
    sum([1 for word in words if is_triangle_word(word)])
)
