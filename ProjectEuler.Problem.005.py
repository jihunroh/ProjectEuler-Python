from math import sqrt

def Factorize(n):
    FactorsList = [1, n]
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.append(divisor)
            if (int(n / divisor) != divisor):
                FactorsList.append(int(n / divisor))
    FactorsList.sort()
    return FactorsList

def DecimalNotation(n):
    divisor = 2
    DecimalNotationList = {}
    
    while not n == 1:
        if n % divisor == 0:
            try:
                DecimalNotationList[divisor] += 1
            except KeyError:
                DecimalNotationList[divisor] = 1
            n = n / divisor
        else:
            divisor += 1
    return DecimalNotationList

def getGCDLCM(Type, NumberList):
    NumberDecList, Factors, Result = [], {}, 1
    
    for x in NumberList:
        NumberDecList.append(DecimalNotation(x))

    for entry_i in NumberDecList:
        for key in entry_i.keys():
            Temp = []
            for entry_j in NumberDecList:
                try:
                    Temp.append(entry_j.get(key, 0))
                    Factors[key] = Type == 'GCD' and min(Temp)or max(Temp)
                except:
                    pass
    
    for factor, power in Factors.items():
        Result *= pow(factor, power)
    return Result

print(getGCDLCM('LCM', range(1,21)))