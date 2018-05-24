from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true_value
from itertools import permutations

Answer(
    int(''.join(map(str, first_true_value(permutations(list(range(10))), None, lambda enum: enum[0] == 1000000 - 1))))
)
