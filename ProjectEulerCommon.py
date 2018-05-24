import time, inspect
from itertools import islice, groupby
start_time = time.time()

def Answer(answer):
    filename = inspect.getmodule(inspect.stack()[1][0]).__file__
    print("------------------------------------------------")
    print("   " + filename)
    print("   The Answer is: %s" %answer)
    print("   Time Elasped: %ssec" %(time.time() - start_time))
    print("------------------------------------------------")

def product(numberlist):
    prod = 1
    for n in numberlist:
        prod *= int(n)
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

def is_palindromic(n):
    n = str(n)
    for i in range(0, len(n)):
        if not n[i] == n[len(n) - i - 1]:
             return False
    return True

def max_generator(finite_generator):
    g = finite_generator()
    max_value = next(g)
    for value in g:
        if value > max_value:
            max_value = value
    return max_value

def nth(iterable, n, default=None):
    # Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

def all_equal(iterable):
    # Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def quantify(iterable, pred=bool):
    # Count how many times the predicate is true"
    return sum(map(pred, iterable))

def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.

    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
    return next(filter(pred, iterable), default)

def first_true_index(iterable, default=False, pred=None):
    iterable = enumerate(iterable)
    return next(filter(pred, iterable), default)[0]

def first_true_value(iterable, default=False, pred=None):
    iterable = enumerate(iterable)
    return next(filter(pred, iterable), default)[1]
