import time
T0 = time.clock()

def f(money, coins):
    i, count = 0, 0

    if (len(coins) == 1):
        if money % coins[0] == 0:
            return 1
        else:
            return 0

    while money - coins[0] * i >= 0:
        temp = f(money - coins[0] * i, coins[1:])
        count += temp
        i += 1
    return count

print(f(200, [200, 100, 50, 20, 10, 5, 2, 1]))
    
print('The execution time is', time.clock()-T0)