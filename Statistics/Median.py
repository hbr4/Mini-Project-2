from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition

def median(num):
    num1 = sorted(num)
    values = len(num1)
    num1.sort()

    if values % 2 == 0:
        median1 = num1[values//2]
        median2 = num1[int(subtraction((values // 2), 1))]
        median = division(addition(median1, median2),2)

    else:
        median = num1[values//2]

    return median



