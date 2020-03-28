from Statistics.PopulationMean import populationmean
from Calculator.Division import division
from Calculator.Square import squaring


def variance(num):
    try:
        pop_mean = populationmean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + squaring(i - pop_mean)
        return round(division(x, num_values), 3)
    except ValueError:
        print("Error with data")
