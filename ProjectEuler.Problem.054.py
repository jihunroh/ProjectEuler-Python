from ProjectEulerCommons.Base import *
from collections import OrderedDict
from operator import itemgetter

with open('ProjectEuler.Problem.054.poker.txt', 'r') as f:
    hands_list = [line.replace('\n', '').split(' ') for line in f.readlines()]

def rank_hand(hand): # hand = ['AS', 'KD', 'TD', 'JD', '8H']
    hand = list(map(lambda card: (int(card[0].replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')), card[1]), hand))
    hand = [(value, [card[1] for card in list(group)])  for value, group in groupby(sorted(hand, reverse = True), key = lambda card: card[0])]
    hand = sorted(hand, key = lambda card: (len(card[1]), card[0]), reverse = True) # [(4, ['S', 'H', 'D', 'C']), (3, ['S'])]

    values_list = [card[0] for card in hand for i in card[1]]
    suits_list = [suit for card in hand for suit in card[1]]

    is_straight = values_list == list(range(values_list[0], values_list[-1] - 1, -1))
    is_flush = all_equal(suits_list)

    if is_straight and is_flush:    # Royal Flush and Straight Flush
        return [9] + values_list
    elif len(hand[0][1]) == 4:      # Four of a Kind
        return [8] + values_list
    elif len(hand[0][1]) == 3 and len(hand[1][1]) == 2: # Full House
        return [7] + values_list
    elif is_flush:                  # Flush
        return [6] + values_list
    elif is_straight:               # Straight
        return [5] + values_list
    elif len(hand[0][1]) == 3 and len(hand[1][1]) == 1: # Three of a Kind
        return [4] + values_list
    elif len(hand[0][1]) == 2 and len(hand[1][1]) == 2: # Two Pairs
        return [3] + values_list
    elif len(hand[0][1]) == 2 and len(hand[1][1]) == 1: # One Pair
        return [1] + values_list
    return [0] + values_list

Answer(
    sum([rank_hand(hands[:5]) > rank_hand(hands[5:]) for hands in hands_list])
)

"""
------------------------------------------------
   ProjectEuler.Problem.054.py
   The Answer is: 376
   Time Elasped: 0.3121659755706787sec
------------------------------------------------
"""
