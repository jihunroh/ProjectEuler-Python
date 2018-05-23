from itertools import permutations

def is_pandigital(number):
    return (len(number) == 9 and '1' in number and '2' in number and '3' in number and '4' in number and '5' in number and '6' in number and '7' in number and '8' in number and '9' in number)

def generate_pandigital_digits_list():
    return permutations(range(1, 10))

def generate_pandigital():
    g = permutations(range(1, 10))
    while True:
        yield int(''.join(map(str, next(g))))