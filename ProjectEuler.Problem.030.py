from ProjectEulerCommon import Answer
from itertools import count

Answer(
    sum([n for n in range(1, 9**5 * next(m for m in count(1) if 10**(m - 1) > 9**5 * m) - 1) if n == sum([int(digit)**5 for digit in list(str(n))])]) - 1
)
