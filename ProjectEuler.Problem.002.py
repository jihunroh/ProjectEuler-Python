import time
T0 = time.clock()

def Fibonacci(n):
    if n < 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

n, ans, Pointer = 1, 0, Fibonacci(0)

while (Pointer < 4000000):
    if Pointer % 2 == 0:
        ans += Pointer
    n += 1
    Pointer = Fibonacci(n)

print('Answer is', ans)
print('The execution time is', time.clock()-T0)