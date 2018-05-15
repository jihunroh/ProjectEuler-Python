def is_Palindromic(n):
    n = str(n)
    for i in range(0,len(n)):
        if not n[i] == n[len(n) - i - 1]:
             return False
    return True
def floor(n):
    return int(n) 
def dec2bin(n):
    n = int(n)
    m = n
    output = ''
    while not m == 1:
        output = str(m % 2) + output
        m = int(m / 2)
    output = str(1) + output
    return int(output)
total = [n for n in range(1, 1000000) if is_Palindromic(n) and is_Palindromic(dec2bin(n))]
print(sum(total))