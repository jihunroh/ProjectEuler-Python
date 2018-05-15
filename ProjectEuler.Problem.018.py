import time
T0 = time.clock()
def num2char(n):
    if n == 1:
        return 'One'
    elif n == 2:
        return 'Two'
    elif n == 3:
        return 'Three'
    elif n == 4:
        return 'Four'
    elif n == 5:
        return 'Five'
    elif n == 6:
        return 'Six'
    elif n == 7:
        return 'Seven'
    elif n == 8:
        return 'Eight'
    elif n == 9:
        return 'Nine'
    elif n == 10:
        return 'Ten'
    elif n == 20:
        return 'Twenty'
    elif n == 30:
        return 'Thirty'
    elif n == 40:
        return 'Forty'
    elif n == 50:
        return 'Fifty'
    elif n == 60:
        return 'Sixty'
    elif n == 70:
        return 'Seventy'
    elif n == 80:
        return 'Eighty'
    elif n == 90:
        return 'Ninety'
    elif n == 100:
        return 'Hundred'
    elif n == 11:
        return 'Eleven'
    elif n == 12:
        return 'Twelve'
    elif n == 13:
        return 'Thirteen'
    elif n == 14:
        return 'Fourteen'
    elif n == 15:
        return 'Fifteen'
    elif n == 16:
        return 'Sixteen'
    elif n == 17:
        return 'Seventeen'
    elif n == 18:
        return 'Eighteen'
    elif n == 19:
        return 'Nineteen'
    elif n == 1000:
        return 'Thousand'
    else:
        return None

def num2phrase(n):
    ## 1000의 자리
    phrase = num2char(int(n / 1000)) + num2char(1000) if int(n / 1000) != 0 else ''
    n = n - int(n / 1000) * 1000

    ## 100의 자리
    phrase += num2char(int(n / 100)) + num2char(100) if int(n / 100) != 0 else ''
    
    ## and 처리
    phrase += 'And' if int(n / 100) != 0 and n % 100 != 0 else ''
    n = n - int(n / 100) * 100 
        
    ## 10의 자리
    if int(n / 10) == 1:
        phrase += num2char(n)
    else:
        phrase += num2char(int(n / 10) * 10) if int(n / 10) != 0 else '' 
    n = n - int(n / 10) * 10 if int(n / 10) != 1 else 0

    ## 1의 자리
    phrase += num2char(n) if n != 0 else ''
    return phrase
length = 0

for i in range(1,1001):
    data = num2phrase(i)
    length += len(data) 
print(length)
print('The execution time is', time.clock()-T0)