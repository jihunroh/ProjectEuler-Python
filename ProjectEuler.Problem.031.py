from ProjectEulerCommons.Base import *

def count_ways(money, coins):
    if len(coins) == 1:
        return 1 if money % coins[0] == 0 else 0
    return sum([count_ways(money - coins[0] * cnt_first_coin, coins[1:]) for cnt_first_coin in range(0, first_true(count(0), pred = lambda x: money - coins[0] * x < 0))])

Answer(
    count_ways(200, [200, 100, 50, 20, 10, 5, 2, 1])
)

"""
------------------------------------------------
   ProjectEuler.Problem.031.py
   The Answer is: 73682
   Time Elasped: 0.07277131080627441sec
------------------------------------------------
"""
