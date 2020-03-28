from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance


def stddev(num):
    variance_num = variance(num)
    return round(squarerooting(variance_num), 4)
