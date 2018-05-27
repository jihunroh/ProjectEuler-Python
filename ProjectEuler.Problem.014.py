from ProjectEulerCommons.Base import *

dict_collatz_sequence_length = {
    13: 10
}

def get_collatz_sequence_length(n):
    global dict_collatz_sequence_length
    
    next_n, length = n, 1

    while next_n != 1:
        if next_n in dict_collatz_sequence_length:
            dict_collatz_sequence_length[n] = length + dict_collatz_sequence_length[next_n] - 1
            return length + dict_collatz_sequence_length[next_n] - 1
        next_n = int(next_n / 2) if next_n % 2 == 0 else 3 * next_n + 1
        length += 1

    dict_collatz_sequence_length[n] = length
    return length

Answer(
    max_index([(x, get_collatz_sequence_length(x)) for x in range(1, 1000000 + 1)])[0]
)

"""
------------------------------------------------
   ProjectEuler.Problem.014.py
   The Answer is: 837799
   Time Elasped: 3.183487892150879sec
------------------------------------------------
"""
