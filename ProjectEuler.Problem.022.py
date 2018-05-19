from ProjectEulerCommon import Answer

alphabet2order = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def alphabet_order_sum(name):
    return sum([alphabet2order[alphabet] for alphabet in name])

with open('ProjectEuler.Problem.022.names.txt', 'r') as f:
    names = [line.replace('"', '').split(',') for line in f.readlines()][0]
names.sort()

Answer(
    sum([(i + 1) * alphabet_order_sum(name) for i, name in enumerate(names)])
)
