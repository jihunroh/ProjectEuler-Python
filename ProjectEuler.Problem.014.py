import time

def IterateTerm(n):
    if n % 2 == 0: #even
        return n / 2
    else:
        return 3 * n + 1
def CountTerms(n):
    count = 1
    while n != 1:
        n = IterateTerm(n)
        count += 1
    return count
T0 = time.clock()

data = [1,1]

for i in range(1, 1000000):
    cnt = CountTerms(i)
    #print(i, cnt)
    if cnt > data[1]:
        data = [i, cnt]

print(data)
print('The execution time is', time.clock()-T0)

"""
[837799, 525]
The execution time is 202.311231011
"""