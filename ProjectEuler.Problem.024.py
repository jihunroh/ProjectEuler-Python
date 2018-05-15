def permutations(number):
    number
    if len(number) <= 1:
        yield number
    else:
        for perm in permutations(number[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + number[0:1] + perm[i:]
perms = permutations('0123456789')
List = []
while True:
    try:
        List.append(next(perms))
    except:
        break
List.sort()
print(List[1000000-1])