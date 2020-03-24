from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance

def stddev(num):
    variance_num = variance(num)
    return squarerooting(variance_num)

