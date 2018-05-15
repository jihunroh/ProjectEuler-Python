import time
T0 = time.clock()
from decimal import * 

def count_recurring_length(n):
    i, numberList = 0, []
    while True:
        getcontext().prec = 10 + i #abnormalous effect
        temp = Decimal('1') / Decimal(str(n)) * (Decimal(10) ** Decimal(i)) % Decimal(1)
        if temp == 0:
            return 0
        if temp in numberList:
            return i - numberList.index(temp)   
        numberList.append(temp)
        i += 1
cycleList, previous_max = [], 0

for i in range(1,1000):
    candi_max = count_recurring_length(i)
    if previous_max < candi_max:
        candi_d = i
        previous_max = candi_max
    if i % 100 == 0:
        print(i)
print('d value', candi_d,'has', previous_max, 'recurring digits')

print('The execution time is', time.clock()-T0)