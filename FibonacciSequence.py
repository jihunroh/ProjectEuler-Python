# Fibonacci numbers module

def Generator(max_number = None):
    a, b = 1, 1
    yield a
    yield b
    while True:
        temp = a
        a = b
        b = temp + b
        if (max_number is not None and b > max_number):
            break
        else:
            yield b