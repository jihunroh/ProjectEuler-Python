import time
from math import sqrt
T0 = time.clock()
def iterate_formula(a, b, n):
    return n ** 2 + a * n + b

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
def count_prime(a, b):
    n = 0
    while is_prime(iterate_formula(a, b, n)):
        n += 1
    return n

max = [0, 0, 0]
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        cnt = count_prime(a, b)
        if cnt > max[0]:
            max = [cnt, a, b]
print(max[1] * max[2])
print('The execution time is', time.clock()-T0)
#-59231
#The execution time is 17.1108356191