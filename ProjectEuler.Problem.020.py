def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

sum2, num = 0, str(2**1000)
for i in range(len(num)):
    sum2 += int(num[i])
print(sum2)
