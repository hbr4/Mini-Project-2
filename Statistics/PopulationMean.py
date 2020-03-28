from Calculator.Division import division


def populationmean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)

    except ValueError:
        print("Error with data")