import time
from eulerlibs import combination
T0 = time.clock()
count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if combination(n, r) > 1000000:
            count += 1
print(count)
print('The execution time is', time.clock()-T0)
#The execution time is 0.00391685299776