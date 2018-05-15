def alphabeticalValue(c):
    return ord(c) - 64

raw_data = open('names.txt')
for data in raw_data:
    pass
data = data.replace('"', '')
data = data.split(',')
data.sort()
score = alphascore = 0
#data = ['AAA','BBB', 'CCC']

for x in data:
    for y in x: #낱개 글자
        alphascore += alphabeticalValue(y)
    orderscore = data.index(x) + 1
    score += alphascore * orderscore
    alphascore = orderscore = 0
print(score)