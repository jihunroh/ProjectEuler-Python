from ProjectEulerCommon import Answer
from ProjectEulerCommon import first_true_index
from FibonacciSequence import generate_fibonacci

Answer(
    first_true_index(generate_fibonacci(), pred = lambda enum: len(str(enum[1])) == 1000) + 1
)
