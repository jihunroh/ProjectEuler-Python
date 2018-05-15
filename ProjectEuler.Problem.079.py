import time
T0 = time.clock()
def num2digitallist(n):
    digitallist = list(str(n))
    for i in range(len(digitallist)):
        digitallist[i] = int(digitallist[i])
    return digitallist

keylog, raw_data = [], open('keylog.txt')


for data in raw_data:
    keylog.append(int(data.replace('\n', '')))



print('The execution time is', time.clock()-T0)