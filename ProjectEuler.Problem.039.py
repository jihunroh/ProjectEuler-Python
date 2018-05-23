from ProjectEulerCommon import Answer
from ProjectEulerCommon import max_index

def generate_triangle_length_for_perimeter(p):
    for a in range(1, p - 2):
        for b in range(a, p - a - 1):
            if a**2 + b**2 == (p - a - b)**2:
                yield (a, b, p - a - b)

Answer(
    max_index([(p, sum(1 for i in generate_triangle_length_for_perimeter(p))) for p in range(3, 1000 + 1)])[0]
)
