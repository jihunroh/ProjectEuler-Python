from ProjectEulerCommons.Base import Answer
from ProjectEulerCommons.Base import nth
from ProjectEulerCommons.PrimeNumbers import generate_prime

Answer(
    nth(generate_prime(), 10001 - 1)
)

"""
------------------------------------------------
   ProjectEuler.Problem.007.py
   The Answer is: 104743
   Time Elasped: 0.3361032009124756sec
------------------------------------------------
"""
