from ProjectEulerCommon import Answer
from calendar import monthrange

Answer(
    len([(year, month) for year in range(1901, 2000 + 1) for month in range(1, 12 + 1) if monthrange(year, month)[0] == 6])
)
