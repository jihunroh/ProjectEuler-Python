import time, inspect
import itertools
from os.path import basename

start_time = time.time()

def Answer(answer):
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    print("------------------------------------------------")
    print("   " + basename(filename))
    print("   The Answer is: %s" %answer)
    print("   Time Elasped: %ssec" %(time.time() - start_time))
    print("------------------------------------------------")

chain = itertools.chain
count = itertools.count
groupby = itertools.groupby
islice = itertools.islice
permutations = itertools.permutations
takewhile = itertools.takewhile   


def product(numberlist):
    prod = 1
    for n in numberlist:
        prod *= n
    return prod
    
def combination(n, r):
    return int(product(range(r+1, n+1)) / factorial(n-r))

def factorial(n):
    return n * factorial(n-1) if (n != 0 and n != 1) else 1
    
def max_index(key_value_dict):
    if type(key_value_dict) is dict:
        max_key, max_value = next(iter(key_value_dict)), key_value_dict[next(iter(key_value_dict))]
        for key in key_value_dict.keys():
            if key_value_dict[key] > max_value:
                max_key, max_value = key, key_value_dict[key]
        return (max_key, max_value)
    else:
        max_index, max_value = key_value_dict[0][0], key_value_dict[0][1]
        for index in range(len(key_value_dict)):
            if key_value_dict[index][1] > max_value:
                max_index, max_value = key_value_dict[index][0], key_value_dict[index][1]
        return (max_index, max_value)

def max_generator(finite_generator):
    g = finite_generator()
    max_value = next(g)
    for value in g:
        if value > max_value:
            max_value = value
    return max_value

def take(n, iterable):
    return list(islice(iterable, n))

def nth(iterable, n, default=None):
    return next(islice(iterable, n, None), default)

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def quantify(iterable, pred=bool):
    return sum(map(pred, iterable))

def first_true(iterable, default = False, pred = None):
    return next(filter(pred, iterable), default)

def first_true_index(iterable, default = False, pred = None):
    iterable = enumerate(iterable)
    return next(filter(pred, iterable), default)[0]

def first_true_value(iterable, default = False, pred = None):
    iterable = enumerate(iterable)
    return next(filter(pred, iterable), default)[1]

def joined_int(int_list):
    return int(''.join(map(str, int_list)))
