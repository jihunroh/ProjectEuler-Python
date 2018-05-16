from ProjectEulerCommon import Answer
from Factors import factorize
from PrimeNumbers import is_prime

Answer(
    max([x for x in factorize(600851475143) if is_prime(x)])
)
