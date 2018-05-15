from math import sqrt
import time

T0 = time.clock()

def is_Prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        return False
    for divisor in [a for a in range(2, int(sqrt(x)) + 1) if not a % 2 == 0 and not a % 3 == 0 and not a % 5 == 0 and not a % 7 == 0]:
        if x % divisor == 0:
            return False
    return True

def SumPrime(UpperBound):
    Number, Sum = 3, 2
    while Number < UpperBound:
        if is_Prime(Number):
            Sum += Number
        else:
            pass
        Number += 2
    return Sum
print(SumPrime(2000000))
print('The execution time is', time.clock()-T0)
"""
142913828922
The execution time is 155.617390392
"""