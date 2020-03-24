from Calculator.Division import division
from Statistics.ZScore import zscore


def correlation(data, data1):
    z = zscore(data)
    z1 = zscore(data1)
    ztot = list(map(lambda x, y: x * y, z, z1))
    corr = division(sum(ztot), len(ztot))
    return corr
