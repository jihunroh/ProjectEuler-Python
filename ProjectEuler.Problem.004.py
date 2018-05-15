import time
T0 = time.clock()

def is_PalindromicNumber(n):
    n = str(n)
    for i in range(0,len(n)):
        if not n[i] == n[len(n) - i - 1]:
             return False
    return True

ans=[]
x = list(range(100, 1000))
x.reverse()
y = x

for i in x:
    for j in y:
        if is_PalindromicNumber(i * j):
            ans.append(i * j)
ans = list(ans)
ans.sort()
print('Answer is', ans[-1])
print('The execution time is', time.clock()-T0)