from ProjectEulerCommon import Answer
from PrimeNumbers import generate_prime, is_prime
from itertools import takewhile, islice

def is_truncatable_prime(n):
    if n in [2, 3, 5, 7]:
        return False
    numberlist = [int(str(n)[i:]) for i in range(1, len(str(n)))] + [int(str(n)[:j]) for j in range(1, len(str(n)))]
    for n in numberlist:
        if not is_prime(n):
            return False
    return True

def generate_truncatable_prime():
    g = generate_prime()
    while True:
        temp = next(g)
        if is_truncatable_prime(temp):
            yield temp

Answer(
    sum([num for num in islice(generate_truncatable_prime(), 11)])
)
