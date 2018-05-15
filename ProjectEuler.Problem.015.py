import time

T0 = time.clock()
"""
(0,0) (0,1)
(1,0) (1,1)
"""
dim = 21
matrix = [[None] * dim for i in range(dim)]

for i in range(dim):
    for j in range(0, i+1):
        if (i == 0 and j == 0):
            matrix[i][j] = 1
        elif i == 0 or j == 0:
            matrix[i][j] = 1
        elif i == j:
            matrix[i][j] = matrix[i][j-1] * 2
        else:
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

print(matrix[dim-1][dim-1])
print('The execution time is', time.clock()-T0)
"""
137846528820
The execution time is 0.00137974112932
"""