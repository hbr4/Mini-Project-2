from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaring


def variance(num):
    values = len(num)
    sum=0
    for i in range(values):
        sum = addition(sum, num[i])

    mean = division(sum, values)
    return mean

    sum2=0
    for i in range(values):
        sum2 = addition(squaring(num[i]), sum2)

    var = subtraction(division(sum2, values), squaring(mean))
    return var



