# Fibonacci numbers module

def generate_fibonacci(max_number = None):            
    prev, curr = 0, 1
    while True:
        if (max_number is not None and curr > max_number):
            break
        else:
            yield curr
        prev, curr = curr, prev + curr