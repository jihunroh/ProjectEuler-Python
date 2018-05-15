import time
T0 = time.clock()

x, last = [x ** x for x in range(1, 1001)], ''

for i in range(10):
    last = last + str(sum(x))[- 10 + i] 

print(last)
print('The execution time is', time.clock()-T0)

"""
9110846700
The execution time is 0.168748171466
"""