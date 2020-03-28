from Statistics.StandardDeviation import stddev
from Calculator.SquareRoot import squarerooting
from Statistics.PopulationMean import populationmean


def confidence_low(num):
    values = len(num)
    z = 1.96
    stdev1 = stddev(num)
    avg = populationmean(num)
    return (avg - (z * stdev1)) / (squarerooting(values))

