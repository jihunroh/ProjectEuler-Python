from ProjectEulerCommon import Answer
from itertools import permutations

def canbe_equation(pandigital, product_length):
    product = int(''.join(map(str, pandigital[9 - product_length:])))
    for multiplicand_length in range(1, 9 - product_length):
        multiplicand = int(''.join(map(str, pandigital[:multiplicand_length])))
        multiplier   = int(''.join(map(str, pandigital[multiplicand_length:9 - product_length])))
        if product == multiplicand * multiplier:
            return True
    return False

Answer(
    sum(set([
        int(''.join(map(str, pandigital[9 - product_length:])))
        for product_length in range(4, 5)
        for pandigital in permutations(range(1, 10))
        if canbe_equation(pandigital, product_length)
    ]))
)
