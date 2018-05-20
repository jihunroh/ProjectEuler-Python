from ProjectEulerCommon import Answer

def generate_permutations(digit_lists):
    if len(digit_lists) == 1:
        yield digit_lists
    else:
        for i, digit in enumerate(digit_lists):
            for sub_permutation in generate_permutations(digit_lists[:i] + digit_lists[i+1:]):
                yield [digit] + sub_permutation

Answer(
    ''.join([str(digit) for digit in next(n for i, n in enumerate(generate_permutations(list(range(10)))) if i == 1000000 - 1)])
)
