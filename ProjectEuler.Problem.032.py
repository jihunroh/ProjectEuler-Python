import time
from eulerlibs import factorial
T0 = time.clock()
print(factorial(9))

print('The execution time is', time.clock()-T0)