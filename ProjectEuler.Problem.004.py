from ProjectEulerCommon import Answer
from ProjectEulerCommon import is_palindromic

Answer(
    max([x * y  for x in range(100,1000) for y in range(100,1000) if is_palindromic(x * y)])
)
