from ProjectEulerCommons.Base import *

Answer(
    sum([n for n in range(10, factorial(9) * (first_true(count(1), pred = lambda digits_length: factorial(9) * digits_length < 10**(digits_length - 1)) - 1)) if sum([factorial(int(digit)) for digit in str(n)]) == n])
)

"""
------------------------------------------------
   ProjectEuler.Problem.034.py
   The Answer is: 40730
   Time Elasped: 23.121175289154053sec
------------------------------------------------
"""

# 숫자                  자릿수팩토리얼 합
# 1~9			        1~362,880	    1	    9
# 10~99			        2~725,76        10      99
# 100~999 		    	3~1,088,640     100     999
# 1,000~9,999	    	4~1,451,520     1000	9999
# 10,000~99,999	    	5~1,814,400 	10000	99999
# 100,000~999,999	    6~2,177,280 	100000	999999
# 1,000,000~9,999,999	7~2,540,160     1000000	2540160
# 10,000,000~99,999,999	8~2,903,040     x       x
