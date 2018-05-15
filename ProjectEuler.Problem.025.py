import time

def NextFibonacci(terms):
    return sum(terms)

terms, length, i = [1, 1], 1, 2 
T0 = time.clock()

while not length == 1000:
    next = NextFibonacci(terms) 
    terms.pop(0)
    terms.append(next)
    length = len(str(terms[1]))
    i += 1
    
print(terms[1], i)    

print('The execution time is', time.clock()-T0)