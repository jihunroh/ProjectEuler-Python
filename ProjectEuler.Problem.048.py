from ProjectEulerCommon import Answer
Answer(
    str(sum([n**n for n in range(1, 1000 + 1)]))[-10:]
)
