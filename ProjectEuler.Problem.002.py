from ProjectEulerCommon import Answer
from FibonacciSequence import generate_fibonacci

Answer(
    sum([x for x in generate_fibonacci(4000000) if x % 2 == 0])
)
