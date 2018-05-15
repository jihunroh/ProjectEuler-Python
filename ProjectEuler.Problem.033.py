import time
from eulerlibs import prod, getGCD
T0 = time.clock()
nums, dens = [], []
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        for n in str(numerator).replace('0', ''):
            if n in str(denominator):
                num, den = int(str(numerator).replace(n, '', 1)), int(str(denominator).replace(n, '', 1))
                if den == 0:
                    continue
                if num / den == numerator / denominator :
                    nums.append(numerator)
                    dens.append(denominator)
GCD = getGCD([prod(nums), prod(dens)])
print(int(prod(dens) / GCD))
print('The execution time is', time.clock()-T0)
#100
#The execution time is 0.0247488906133