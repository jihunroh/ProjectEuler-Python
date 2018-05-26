from ProjectEulerCommons.Base import Answer

with open('ProjectEuler.Problem.067.triangle.txt', 'r') as f:
    triangle = [list(map(int, line.split(' '))) + [0] * (15 - 1 - i) for i, line in enumerate([line.replace('\n', '') for line in f.readlines()])]

def reduce_to_local_maximum_path(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        return reduce_to_local_maximum_path(triangle[0:len(triangle) - 2] + [[step + max(triangle[-1][i:i+2]) for i, step in enumerate(triangle[-2]) if step is not 0]])

Answer(
    reduce_to_local_maximum_path(triangle)
)

"""
------------------------------------------------
   ProjectEuler.Problem.067.py
   The Answer is: 7273
   Time Elasped: 0.009425640106201172sec
------------------------------------------------
"""
