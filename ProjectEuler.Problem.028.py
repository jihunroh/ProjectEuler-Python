def leftup(n):
    return  4 * n ** 2 - 6 * n + 3
    # 1, 7, 21, 43

def leftdown(n):
    return  4 * n ** 2 - 8 * n + 5
    # 1, 5, 17, 37

def rightup(n):
    return  4 * n ** 2 - 4 * n + 1
    # 1, 9, 25, 49

def rightdown(n):
    return  4 * n ** 2 - 10 * n + 7
    # 1, 3, 13, 31

def diagonalsum(n): # n is square matrix dimension
    ans = 1
    for i in range(2, int(n / 2) + 2):
        ans += leftup(i) + leftdown(i) + rightup(i) + rightdown(i)
    return ans
print(diagonalsum(1001))
