from ProjectEulerCommon import Answer
from itertools import count

def count_ways(money, coins):
    if len(coins) == 1:
        return 1 if money % coins[0] == 0 else 0
    return sum([count_ways(money - coins[0] * cnt_first_coin, coins[1:]) for cnt_first_coin in range(0, next(cnt_first_coin for cnt_first_coin in count(0) if money - coins[0] * cnt_first_coin < 0))])

Answer(
    count_ways(200, [200, 100, 50, 20, 10, 5, 2, 1])
)
