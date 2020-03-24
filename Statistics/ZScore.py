from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.PopMean import populationmean
from Statistics.StandardDeviation import stddev


def zscore(num):
    zmean = populationmean(num)
    sd = stddev(num)
    zlist = []
    for x in num:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist
