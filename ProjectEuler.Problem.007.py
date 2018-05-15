from math import sqrt

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

def getNthPrime(n):
    Number, i = 3, 2
    while not i == n + 1:
        if is_Prime(Number):
            i += 1
        else:
            pass
        Number += 2
    return Number - 2

print(getNthPrime(10001))