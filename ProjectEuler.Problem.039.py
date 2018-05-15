import time
T0 = time.clock()
def count_sides(p):
    count = 0
    for a in range(1, p - 2):
        for b in range(a, p - a - 1):
            c = p - a - b
            if c < a or c < b:
                break
            if a ** 2 + b ** 2 == c ** 2:
                count += 1
                break
    return count
previous_sides = 0
for i in range(1, 1001):
    candi_sides = count_sides(i)
    if previous_sides < candi_sides:
        previous_sides, candi_p = candi_sides, i
print(candi_p, previous_sides)
print('The execution time is', time.clock()-T0)

#840 8
#The execution time is 52.6848875001