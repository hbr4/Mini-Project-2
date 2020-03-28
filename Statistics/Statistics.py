from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
from Statistics.Variance import variance
from Statistics.PopulationMean import populationmean
from Statistics.ZScore import zscore
from Statistics.Correlation import correlation
from Statistics.Skewness import skewness
from Statistics.ConfidenceLow import confidence_low
from Statistics.ConfidenceUp import confidence_up

class Statistics(Calculator):
    data = []

    def __init__(self):
        pass

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def populationmean(self, data):
        self.result = populationmean(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    def correlation(self, data, data1):
        self.result = correlation(data, data1)
        return self.result

    def skewness(self,data):
        self.result = skewness(data)
        return self.result

    def confidence_up(self,data):
        self.result = confidence_up(data)
        return self.result

    def confidence_low(self,data):
        self.result = confidence_low(data)
        return self.result

    pass