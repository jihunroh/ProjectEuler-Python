from ProjectEulerCommon import Answer
from ProjectEulerCommon import is_palindromic

Answer(
    sum([num for num in range(1000000) if is_palindromic(num) and is_palindromic(bin(num)[2:])])
)
