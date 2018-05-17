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
    return n * factorial(n-1) if n is not 1 else 1