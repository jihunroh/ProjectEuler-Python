from math import sqrt

def factorize(n):
    FactorsList = [1, n]
    for divisor in [a for a in range(2, int(sqrt(n)) + 1)]:
        if n % divisor == 0:
            FactorsList.append(divisor)
            if (int(n / divisor) != divisor):
                FactorsList.append(int(n / divisor))
    FactorsList.sort()
    return FactorsList

def prime_factorize(n):
    divisor = 2
    prime_factor_dict = {}
    
    while not n == 1:
        if n % divisor == 0:
            try:
                prime_factor_dict[divisor] += 1
            except KeyError:
                prime_factor_dict[divisor] = 1
            n = n / divisor
        else:
            divisor += 1
    return prime_factor_dict

def get_LCM(number_list):
    factors, result = {}, 1
    prime_factors_dict_list = [prime_factorize(x) for x in number_list]
    
    for prime_factors_dict in prime_factors_dict_list:
        for factor in prime_factors_dict.keys():
            factors[factor] = max([prime_factors_dict2.get(factor, 0) for prime_factors_dict2 in prime_factors_dict_list])
    
    for factor, power in factors.items():
        result *= pow(factor, power)
    return result

def get_GCD(numberlist):
    return int(prod(numberlist) / getLCM(numberlist))
