import time
T0 = time.clock()
global triangular_number_list
triangular_number_list = [0.5 * x * (x + 1) for x in range(1000)]

def alphabeticalValue(c):
    return ord(c) - 64

def is_triangular_number(n):
    return n in triangular_number_list

raw_data = open('words.txt')
for data in raw_data:
    pass
data = data.replace('"', '')
data = data.split(',')
data.sort()
count, i = 0, 0 

for item in data:
    value = 0
    for c in item:
        value += alphabeticalValue(c)
    if is_triangular_number(value):
        count += 1
    i += 1
print(count)

print('The execution time is', time.clock()-T0)