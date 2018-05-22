import time, inspect
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
    max_key, max_value = next(iter(key_value_dict)), key_value_dict[next(iter(key_value_dict))]
    for key in key_value_dict.keys():
        if key_value_dict[key] > max_value:
            max_key, max_value = key, key_value_dict[key]
    return (max_key, max_value)

def is_palindromic(n):
    n = str(n)
    for i in range(0, len(n)):
        if not n[i] == n[len(n) - i - 1]:
             return False
    return True
