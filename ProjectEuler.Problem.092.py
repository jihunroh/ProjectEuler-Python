from ProjectEulerCommons.Base import *

arrive_at_89_list, arrive_at_1_list = set([89]), set([1])

def arrive_at_89(n):
    global arrive_at_1_list, arrive_at_89_list
    generated_list = []
    
    while True:
        generated_list.append(n)
        n = sum(int(digit)**2 for digit in str(n))

        if n in arrive_at_89_list:
            arrive_at_89_list.update(generated_list)
            return True
        elif n in arrive_at_1_list:
            arrive_at_1_list.update(generated_list)
            return False

Answer(
    sum(arrive_at_89(n) for n in range(1, 10000000))
)

"""
------------------------------------------------
   ProjectEuler.Problem.092.py
   The Answer is: 8581146
   Time Elasped: 57.221978187561035sec
-----------------------------------------------
"""
