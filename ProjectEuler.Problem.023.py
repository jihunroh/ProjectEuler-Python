import time
from math import sqrt

T0 = time.clock()
def factorize(n):
    FactorsList = set([1])
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.add(divisor)
            FactorsList.add(int(n / divisor))
            #FactorsList.append(divisor)
            #FactorsList.append(int(n / divisor))
    return FactorsList

def is_abundant(n):
    return sum(factorize(n)) > n
def list_abundants():
    return [x for x in range(1, 28124) if is_abundant(x)] #20161
def possible_sums_of_two_abundant(abundantList):
    total = set([])
    for i in range(len(abundantList)):
        for j in range(i, len(abundantList)):
            s = abundantList[i]+abundantList[j]
            if s < 28124:
                total.add(s)
    return total
print(sum(range(1, 28124)) - sum(possible_sums_of_two_abundant(list_abundants())))
print('The execution time is', time.clock()-T0)
#4179871
#The execution time is 13.2483100259
