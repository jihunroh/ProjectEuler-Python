from ProjectEulerCommon import Answer
from PandigitalNumbers import generate_pandigital

def get_concatenated_product(multiplicand):
    j, concat_product = 1, ''

    while len(concat_product) < 9:
        concat_product += str(int(multiplicand) * j)
        j += 1

    return concat_product if len(concat_product) == 9 else None

def is_concatenated_product(pandigital_num):    
    for i in range(1, 8):
        multiplicand = str(pandigital_num)[:i]
        if get_concatenated_product(multiplicand) == str(pandigital_num):
            return True
        else:
            continue
    return False

Answer(
    max([pandigital_num for pandigital_num in generate_pandigital() if is_concatenated_product(pandigital_num)])
)
