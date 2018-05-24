from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true
from PandigitalNumbers import generate_pandigital
from PrimeNumbers import is_prime

Answer(
    first_true([first_true(generate_pandigital(digit, reverse = True), False, lambda n: is_prime(n)) 
    for digit in range(9, 0, -1)], False, lambda x: x != False)
)
