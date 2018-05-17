from ProjectEulerCommon import Answer
from PrimeNumbers import generate_prime
from itertools import takewhile

Answer(
    sum([n for n in takewhile(lambda x: x < 2000000, generate_prime())])
)