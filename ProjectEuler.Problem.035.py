from ProjectEulerCommon import Answer
from PrimeNumbers import generate_prime_below, is_prime
from itertools import permutations

def circulations(target_list):
    for i in range(len(target_list)):
        yield target_list[i:] + target_list[:i]

Answer(
    len([n for n in generate_prime_below(1000000) if not False in [is_prime(int(''.join(map(str, circular_num)))) for circular_num in circulations(list(map(int, list(str(n)))))]])
)
