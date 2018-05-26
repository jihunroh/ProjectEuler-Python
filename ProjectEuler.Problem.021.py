from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Factors import factorize

def d(n):
    return 0 if n == 1 else sum(factorize(n)[0:-1])

Answer(
    sum([sum(amicable_pair) for amicable_pair in [(n, d(n)) for n in range(1, 10000) if n == d(d(n)) and n != d(n) and n < d(n)]])
)
