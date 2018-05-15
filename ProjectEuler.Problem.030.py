power = 5

def max_digit(power):
    digit = 1
    while digit < 10 ** digit - 1 and 10 ** (digit - 1) < digit * 9 ** power:
        digit += 1
    return digit - 1
answer, max_digit = [], max_digit(power)

for digit in range(2, max_digit + 1):
    lower_bound = max([digit, 10 ** (digit - 1)])
    upper_bound = min([10 ** digit - 1, digit * 9 ** power])
    for x in range(lower_bound, upper_bound + 1):
        summation = 0
        for digit2 in range(digit):
            summation += int(str(x)[digit2]) ** power
        if x == summation:
            answer.append(x) 

print(sum(answer))
#for i in range(2, digit * 9 ** power):    