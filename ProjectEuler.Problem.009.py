from ProjectEulerCommon import Answer

Answer(
    [a * b * (1000 - a - b) for a in range(1, 1000) for b in range(1, 1000) if a * a + b * b == (1000 - a - b) * (1000 - a - b)][0]
)