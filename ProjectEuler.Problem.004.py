from ProjectEulerCommon import Answer

def is_palindromic(n):
    n = str(n)
    for i in range(0,len(n)):
        if not n[i] == n[len(n) - i - 1]:
             return False
    return True

Answer(
    max([x * y  for x in range(100,1000) for y in range(100,1000) if is_palindromic(x * y)])
)
