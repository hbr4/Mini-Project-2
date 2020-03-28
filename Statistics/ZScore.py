from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def zscore(num):
    z_mean = populationmean(num)
    sd = stddev(num)
    z_list = []
    for x in num:
        z = round(((x - z_mean) / sd), 6)
        z_list.append(z)
    return z_list
