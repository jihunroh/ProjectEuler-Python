from ProjectEulerCommon import Answer
from itertools import permutations

Answer(
    ''.join([str(digit) for digit in next(n for i, n in enumerate(permutations(list(range(10)))) if i == 1000000 - 1)])
)
