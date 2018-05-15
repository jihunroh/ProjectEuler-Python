import time
from eulerlibs import is_prime
T0 = time.clock()
def permutations(number):
    if len(number) <= 1:
        yield number
    else:
        for perm in permutations(number[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + number[0:1] + perm[i:]

def iterate_prime():
    n = 1009
    yield n
    while True:
        n += 2
        if is_prime(n) and n < 10000:
            yield n
i = 0
seq = []
while True:
    primes = iterate_prime() 
    perms = permutations(str(next(primes)))

    while True:
        try:
            next_perm = int(next(perms))
            if is_prime(next_perm) and next_perm > 999:
                seq.append(next_perm)
        except:
            break
    print(seq)
    if i == 3:
       break
    i += 1 

print('The execution time is', time.clock()-T0)