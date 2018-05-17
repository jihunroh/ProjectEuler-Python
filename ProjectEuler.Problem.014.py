from ProjectEulerCommon import Answer

def get_collatz_sequence_length(n):
    length = 1
    while (n is not 1):
        n = int(n / 2) if n % 2 == 0 else 3 * n + 1
        length += 1
    return length
number, max_length = 1, 1

for x in range(1, 1000000 + 1):
    length = get_collatz_sequence_length(x)
    if length > max_length:
        number, max_length = x, length
Answer(
    number
)
