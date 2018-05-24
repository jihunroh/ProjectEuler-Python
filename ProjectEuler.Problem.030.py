from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true
from itertools import count

Answer(
    sum([n for n in range(1, 9**5 * first_true(count(1), None, lambda m: 10**(m - 1) > 9**5 * m) - 1)
    if n == sum([int(digit)**5 for digit in list(str(n))])]) - 1
)
