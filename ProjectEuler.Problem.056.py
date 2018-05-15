import time
T0 = time.clock()
def num2digitallist(n):
    digitallist = list(str(n))
    for i in range(len(digitallist)):
        digitallist[i] = int(digitallist[i])
    return digitallist
candi = 0
for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = sum(num2digitallist(a**b))
        candi = digital_sum if candi < digital_sum else candi
print(candi)
print('The execution time is', time.clock()-T0)
#972
#The execution time is 1.34972735127