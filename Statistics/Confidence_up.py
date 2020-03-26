from Statistics.StandardDeviation import stddev
from Calculator.SquareRoot import squarerooting
from Statistics.PopMean import populationmean

def confidence_up(num):
    values = len(num)
    z = 1.96
    stdev = stddev(num)
    avg = populationmean(num)
    return avg + z * stdev / squarerooting(values)

