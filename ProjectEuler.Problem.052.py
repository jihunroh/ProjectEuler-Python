import time
T0 = time.clock()
def same_digits(List):
    for i in range(len(List)):
        aligned_item = []
        for digit in str(List[i]):
            aligned_item.append(int(digit))
            aligned_item.sort()
        List[i] = aligned_item
    for j in range(len(List)):
        if not List[0] == List[j]:
            return False
    return True
n = 1
while not same_digits([n, n * 2, n * 3, n * 4, n * 5, n * 6]):
    n += 1
print(n)       
        
print('The execution time is', time.clock()-T0)
#142857
#The execution time is 13.5115094654