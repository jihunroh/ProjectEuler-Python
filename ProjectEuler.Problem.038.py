import time
from eulerlibs import is_prime
T0 = time.clock()

def is_pandigital(n):
    numberlist = []
    for i in range(len(n)):
        numberlist.append(int(n[i]))
    numberlist.sort()
    if numberlist == list(range(1, 10)):
        return True
    return False

def concatenate_product(p, prodlist):
    prodlist = [p * prod for prod in prodlist]
    number = ''
    for i in range(len(prodlist)):
        number += str(prodlist[i])
    return number


p, pandigital_list = 2, []

while (p < 1000000000):
    p += 1
    for i in range(2, 10):
        candi_pandigital = concatenate_product(p, range(1, i))
        if is_pandigital(candi_pandigital):
            pandigital_list.append(candi_pandigital)
print([2 * x for x in a])
print('The execution time is', time.clock()-T0)