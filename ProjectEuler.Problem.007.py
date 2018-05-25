from ProjectEulerCommon import Answer
from ProjectEulerCommon import nth
from PrimeNumbers import generate_prime

Answer(
    nth(generate_prime(), 10001 - 1)
)
