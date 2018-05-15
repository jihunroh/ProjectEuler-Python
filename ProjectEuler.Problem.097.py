import time
T0 = time.clock()
def iterate_power10(n):
    max_digit, ans = 10, 1
    
    while True:
        if len(str(ans)) > max_digit:
            ans = cut_digit(ans) 
        ans *= n
        yield cut_digit(ans)
def power10(n, p):
    f = iterate_power10(n)
    for i in range(p):
        ans = next(f)
    return ans
    
def cut_digit(n):
    max_digit = 10
    return int(str(n)[-max_digit:])

print(cut_digit(power10(2,7830457) * 28433) + 1)

print('The execution time is', time.clock()-T0)
#8739992577
#The execution time is 49.2251879109