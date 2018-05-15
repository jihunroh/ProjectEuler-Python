import time
from eulerlibs import is_prime
T0 = time.clock()
def permutations(number):
    number
    if len(number) <= 1:
        yield number
    else:
        for perm in permutations(number[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + number[0:1] + perm[i:]

def merge2str(numberlist):
    result = ''
    for item in numberlist:
        result += str(item)
    return result

candi_list = []

for digit in range(9,0,-1):
    digitlist = merge2str(list(range(1, digit + 1))) 
    perms = permutations(digitlist)
    while True:
        try:
            n = int(next(perms))
            if is_prime(n):
                candi_list.append(n)
        except:
            break
candi_list.sort()
print(candi_list[-1])
print('The execution time is', time.clock()-T0)

#7652413
#The execution time is 3.86956613601