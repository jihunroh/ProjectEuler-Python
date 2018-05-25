from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true
from Factors import prime_factorize
from itertools import count

def find_consecutive_nums():
    n = 3

    while True:
        if len(prime_factorize(n)) == 4:
            if len(prime_factorize(n + 1)) == 4:
                if len(prime_factorize(n + 2)) == 4:
                    if len(prime_factorize(n + 3)) == 4:
                        return (n)
                    else:
                        n += 4
                else:
                    n += 3
            else:
                n += 2
        else:
            n += 1

Answer(
    find_consecutive_nums()
)
