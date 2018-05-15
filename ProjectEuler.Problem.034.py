import time
T0 = time.clock()

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 5040
    elif n == 8:
        return 40320
    elif n == 9:
        return 362880

def sum_of_factorials_of_digits(n):
    n, sum = str(n), 0

    if int(n) < 362880 * list(n).count('9'): #9! = 362880
        return False
    if int(n) < 40320 * list(n).count('8'):
        return False
    if int(n) < 5040 * list(n).count('7'):
        return False
    if int(n) < 720 * list(n).count('6'):
        return False

    for digit in n:
        digit = int(digit)
        sum += factorial(digit)

    if sum == int(n):
        return True
    return False
Total = []
for i in range(3, 1000000):
    if (sum_of_factorials_of_digits(i)):
        Total.append(i)
print(sum(Total))
print('The execution time is', time.clock()-T0)

print([factorial(x) for x in range(1,10)])
# 계산 자릿수 계산
#number = ''
#for n in range(1,11):
#    for i in range(n):
#        number += '1'
#    print(n * 362880, int(number)* 9)
#    if (int(number) * 9 > n * 362880):
#        break
#    number = ''
#print(n)
