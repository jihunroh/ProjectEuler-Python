from ProjectEulerCommon import Answer
from FibonacciSequence import generate_fibonacci

Answer(
    next(i for i, n in enumerate(generate_fibonacci()) if len(str(n)) == 1000) + 1
)
