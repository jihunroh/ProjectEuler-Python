from ProjectEulerCommon import Answer
from ProjectEulerCommon import combination, quantify

def generate_combination():
    for n in range(1, 100 + 1):
        for r in range(2, n - 1):
            yield combination(n, r)

Answer(
    quantify(generate_combination(), pred = lambda x: x > 1000000)
)
