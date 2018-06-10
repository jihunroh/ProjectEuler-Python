import time, inspect
import itertools
from os.path import basename
import math
from functools import reduce

start_time = time.time()

def Answer(answer):
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    print("------------------------------------------------")
    print("   " + basename(filename))
    print("   The Answer is: %s" %answer)
    print("   Time Elasped: %ssec" %(time.time() - start_time))
    print("------------------------------------------------")

ceil = math.ceil
floor = math.floor
sqrt = math.sqrt
log = math.log
chain = itertools.chain
count = itertools.count
cycle = itertools.cycle
groupby = itertools.groupby
islice = itertools.islice
permutations = itertools.permutations
takewhile = itertools.takewhile
zip_longest = itertools.zip_longest

def product(numberslist):
    return reduce(lambda x, y: x * y, numberslist)

def diff(numberlist):
    return abs(numberlist[1] - numberlist[0])

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

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def digits_list(n):
    return [(n // (10**i)) % 10 for i in range(floor(log(n, 10)), -1, -1)] if n != 0 else [0]

def joined_int(int_list):
    return int(''.join(map(str, int_list)))

def last(iterable):
    for item in iterable:
        pass
    return item

def count_summation_way(money, coins):
    if len(coins) == 1:
        return 1 if money % coins[0] == 0 else 0
    return sum([count_summation_ways(money - coins[0] * cnt_first_coin, coins[1:]) for cnt_first_coin in range(0, first_true(count(0), pred = lambda x: money - coins[0] * x < 0))])
