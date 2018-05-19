from ProjectEulerCommon import Answer
from ProjectEulerCommon import factorial

Answer(
    sum([int(digit) for digit in str(factorial(100))])
)
