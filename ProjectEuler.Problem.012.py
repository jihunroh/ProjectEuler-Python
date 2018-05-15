from math import sqrt
import time

def Factorize(n):
    FactorsList = [1, n]
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.append(divisor)
            if (int(n / divisor) != divisor):
                FactorsList.append(int(n / divisor))
    FactorsList.sort()
    return FactorsList

def TriangularNumber(n):
    return sum(range(1,n+1))

T0 = time.clock()
length, i = 0, 1

while length < 500:
    length = len(Factorize(TriangularNumber(i))) - 1
    i += 1
print(TriangularNumber(i-1))
print('The execution time is', time.clock()-T0)
"""
76576500
The execution time is 29.4996305969
"""