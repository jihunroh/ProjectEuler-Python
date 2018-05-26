from itertools import permutations

def is_pandigital(number):
    number = str(number)
    if len(number) == 9:
        return ('1' in number and '2' in number and '3' in number and '4' in number and '5' in number and '6' in number and '7' in number and '8' in number and '9' in number)
    elif len(number) == 8:
        return ('1' in number and '2' in number and '3' in number and '4' in number and '5' in number and '6' in number and '7' in number and '8' in number)
    elif len(number) == 7:
        return ('1' in number and '2' in number and '3' in number and '4' in number and '5' in number and '6' in number and '7' in number)
    elif len(number) == 6:
        return ('1' in number and '2' in number and '3' in number and '4' in number and '5' in number and '6' in number)
    elif len(number) == 5:
        return ('1' in number and '2' in number and '3' in number and '4' in number and '5' in number)
    elif len(number) == 4:
        return ('1' in number and '2' in number and '3' in number and '4' in number)
    elif len(number) == 3:
        return ('1' in number and '2' in number and '3')
    elif len(number) == 2:
        return ('1' in number and '2')
    elif len(number) == 1:
        return ('1' in number)

def generate_pandigital_digits_list(digit_range = range(1, 10)):
    return permutations(digit_range)

def generate_pandigital(digit_range = range(1, 10), reverse = False):
    if reverse:
        g = permutations(reversed(digit_range))
    else:
        g = permutations(digit_range)
    while True:
        yield int(''.join(map(str, next(g))))
