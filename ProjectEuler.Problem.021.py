import time
from math import sqrt

T0 = time.clock()
def func_d(n):
    return sum(Factorize(n))
def Factorize(n):
    FactorsList = [1]
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.append(divisor)
            if (int(n / divisor) != divisor):
                FactorsList.append(int(n / divisor))
    FactorsList.sort()
    return FactorsList

amicableList = []

for i in range(10000):
    candi_pair = func_d(i)
    if func_d(candi_pair) == i and i != candi_pair:
        amicableList.append(i)
        amicableList.append(candi_pair)

print(int(sum(amicableList) / 2))
print('The execution time is', time.clock()-T0)

"""
31626
The execution time is 0.6522305565
"""