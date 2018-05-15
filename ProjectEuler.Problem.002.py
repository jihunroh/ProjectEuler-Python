from ProjectEulerCommon import Answer
import FibonacciSequence

Answer(
    sum([x for x in FibonacciSequence.Generator(4000000) if x % 2 == 0])
)
