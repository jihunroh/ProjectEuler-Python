from ProjectEulerCommon import Answer
from PrimeNumbers import generate_prime_below
from itertools import takewhile

Answer(
    sum([n for n in generate_prime_below(2000000)])
)
