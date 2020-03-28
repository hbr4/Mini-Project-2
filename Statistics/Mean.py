from Calculator.Division import division


def mean(num):
    summation = sum(num)
    values = len(num)
    return round(division(summation, values), 4)
