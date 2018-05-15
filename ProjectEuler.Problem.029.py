import time
T0 = time.clock()

def append_and_remove_duplicated(List, item):
    if not List.count(item) == 0:
        List.remove(item)  
    List.append(item)
    return List
Total = []

for a in range(2, 101):
    for b in range(2, 101):
        append_and_remove_duplicated(Total, a**b)
Total.sort()
print('Answer is', len(Total))
print('The execution time is', time.clock()-T0)