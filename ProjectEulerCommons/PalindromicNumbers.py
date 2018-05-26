def is_palindromic(n):
    n = str(n)
    length = len(n)

    for i in range(0, length):
        if not n[i] == n[length - i - 1]:
             return False
    return True
