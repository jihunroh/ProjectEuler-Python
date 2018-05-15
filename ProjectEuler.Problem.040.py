import time
T0 = time.clock()
def iterate_number():
    i = 1
    while True:
        yield i
        i += 1

def iterate_decimal_fraction():
    g = iterate_number()
    while True:
        n = str(next(g))
        for i in range(len(n)):
            yield n[i]

f, product = iterate_decimal_fraction(), 1

for i in range(1, 1000000 + 1):
    seq = next(f)
    if i == 1 or i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000:
        product *= int(seq)
print(product)
print('The execution time is', time.clock()-T0)