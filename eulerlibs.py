# Euler Libraries module
__all__ = ['combination', 'factorial', 'is_prime', 'iterate_prime', 'get_LCM', 'get_GCD', 'prod', 'is_int']
from math import sqrt

def factorize(n):
    FactorsList = [1, n]
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.append(divisor)
            if (int(n / divisor) != divisor):
                FactorsList.append(int(n / divisor))
    FactorsList.sort()
    return FactorsList
def prime_factorize(n):
    return [x for x in factorize(n) if is_prime(x)]

def is_prime_factor(x, n):
    return n % x == 0 and is_prime(x);

def combination(n, r):
    return int(prod(range(r+1, n+1)) / factorial(n-r))

def factorial(n):
    return prod(range(1, n+1))

def is_prime(x):
    if x < 0:
        return False
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

def iterate_prime():
    n = 2
    yield n
    n = 3
    yield n

    while True:
        n += 2
        if is_prime(n):
            yield n

def prod(numberlist):
    prod = 1
    for n in numberlist:
        prod *= n
    return prod

def get_LCM(numberlist):
    numberdeclist, factors, result = [], {}, 1
    
    for x in numberlist:
        numberdeclist.append(DecimalNotation(x))

    for entry_i in numberdeclist:
        for key in entry_i.keys():
            temp = []
            for entry_j in numberdeclist:
                try:
                    temp.append(entry_j.get(key, 0))
                    factors[key] = max(temp)
                except:
                    pass
    
    for factor, power in factors.items():
        result *= pow(factor, power)
    return result

def get_GCD(numberlist):
    return int(prod(numberlist) / getLCM(numberlist))

def decimal_notation(n):
    divisor = 2
    DecimalNotationList = {}
    
    while not n == 1:
        if n % divisor == 0:
            try:
                DecimalNotationList[divisor] += 1
            except KeyError:
                DecimalNotationList[divisor] = 1
            n = n / divisor
        else:
            divisor += 1
    return DecimalNotationList
def is_int(n):
    return n % 1 == 0
if __name__ == '__main__':
    print('Cannot execute alone')