from ProjectEulerCommons.Base import *

number_word_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def get_number_word(number):
    digits_list = {10**(len(str(number)) - 1 - i): int(digit) for i, digit in enumerate(str(number))}

    result = []
    if digits_list.get(1000) is not None: # 1000자리 처리
        result.append(number_word_dict[digits_list.get(1000)])
        result.append(number_word_dict[1000])
    if digits_list.get(100) is not None and digits_list.get(100) is not 0: # 100자리 처리
        result.append(number_word_dict[digits_list.get(100)])
        result.append(number_word_dict[100])
        if not(digits_list.get(10) is 0 and digits_list.get(1) is 0): # and 처리
            result.append('and')
    if digits_list.get(10) is not None and digits_list.get(10) is not 0: # 10자리 처리
        if digits_list.get(10) == 1: # 10~19 특례
            result.append(number_word_dict[digits_list.get(10) * 10 + digits_list.get(1)])
            return result
        else:
            result.append(number_word_dict[digits_list.get(10) * 10])
    if digits_list.get(1) is not 0: # 1자리 처리
        result.append(number_word_dict[digits_list.get(1)])
    return result

Answer(
    sum([len(''.join(get_number_word(n))) for n in range(1, 1000 + 1)])
)

"""
------------------------------------------------
   ProjectEuler.Problem.017.py
   The Answer is: 21124
   Time Elasped: 0.010972738265991211sec
------------------------------------------------
"""
