import time
from eulerlibs import factorize, prime_factorize
T0 = time.clock()
digits = 4

def iterate_number():
    n = 1
    while True:
        for i in range(digits):
            if not len(prime_factorize(n+i)) == digits:
                n = n + i + 1
                break
            elif i == digits - 1:
                yield(n)
            else:
                continue
        
g = iterate_number()
print(next(g))
#print(prime_factorize(1))
print('The execution time is', time.clock()-T0)
#134043
#The execution time is 25.6277454857
