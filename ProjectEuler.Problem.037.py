import time
from eulerlibs import is_prime, iterate_prime
T0 = time.clock()

def get_truncate_list(n):
    return [int(str(n)[i:]) for i in range(1, len(str(n)))] + [int(str(n)[:j]) for j in range(1, len(str(n)))]
def is_prime_list(numberlist):
    for n in numberlist:
        if not is_prime(n):
            return False
    return True
prime, count, ans = iterate_prime(), 0, []
next(prime) # 2
next(prime) # 3
next(prime) # 5
next(prime) # 7
while True:
    prime_n = next(prime)
    truncatelist = get_truncate_list(prime_n)
    if is_prime_list(truncatelist):
        ans.append(prime_n)
        count += 1
    if count == 11:
        break
print(ans, sum(ans))
print('The execution time is', time.clock()-T0)
#[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397] 748317
#The execution time is 57.0643115767