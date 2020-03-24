from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.StandardDeviation import stddev

def skew(num):
    mean_num = mean(num)
    median_num = median(num)
    stddev_num = stddev(num)
    skew = ((mean_num - median_num) * 3) / stddev_num
    return skew
