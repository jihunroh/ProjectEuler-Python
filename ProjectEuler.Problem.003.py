import time
from math import sqrt

T0 = time.clock()

n = 600851475143

def is_PrimeFactor(x, n):
    if not n % x == 0 or not is_Prime(x):
        return False
    return True


def is_Prime(x):
    if x == 1:
        return False
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        return False
    for divisor in [a for a in range(2, int(sqrt(x)) + 1) if not a % 2 == 0]:
        if x % divisor == 0:
            return False
    return True

FactorRange = list(range(1, int(sqrt(n))))[::2]
Factors = [x for x in FactorRange if is_PrimeFactor(x, n)]
TotalFactors = Factors
for x in Factors :
    if is_Prime(n/x):
        TotalFactors.append(n/x)

print('Answer is', TotalFactors)
print('The execution time is', time.clock()-T0)