from ProjectEulerCommon import Answer
from Factors import factorize

list_abundant = [n for n in range(1, 28123 + 1) if sum(factorize(n)[0:-1]) > n]

print(
    sum(set(range(1, 28123 + 1)) - set([a + b for a in list_abundant for b in list_abundant if a <= b and a + b <= 28123]))
)