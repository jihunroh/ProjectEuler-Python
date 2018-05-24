from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true, all_equal
from itertools import count

Answer(
    next(first_true(range(10 ** (digit - 1), int(10 ** digit / 6)), False, lambda num: all_equal(map(sorted, map(str, [num, num * 2, num * 3, num * 4, num * 5, num * 6])))) 
    for digit in count(2) if first_true(range(10 ** (digit - 1), int(10 ** digit / 6)), False, lambda num: all_equal(map(sorted, map(str, [num, num * 2, num * 3, num * 4, num * 5, num * 6])))) != False)
)
