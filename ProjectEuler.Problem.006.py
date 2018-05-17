from ProjectEulerCommon import Answer

Answer(
    pow(sum(list(range(1, 100 + 1))), 2)  - sum([x * x for x in range(1, 100 + 1)])
)
