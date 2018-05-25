from ProjectEulerCommon import Answer
from Factors import prime_factorize
from itertools import count

Answer(
    next(num for num in count(3)
    if range(num, num + 4) and
    len(prime_factorize(num)) == 4 and
    len(prime_factorize(num + 1)) == 4 and
    len(prime_factorize(num + 2)) == 4 and
    len(prime_factorize(num + 3)) == 4
    )
)
