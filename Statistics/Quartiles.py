from Calculator.Subtraction import subtraction
from Calculator.Division import division


samples = sorted([list])

def find_median(sorted_list):
    indices = []

    values = len(sorted_list)
    median = 0

    if values % 2== 0:
        indices.append(int(values / 2) - 1)
        indices.append(int(values /2))

        median = (sorted_list[indices[0]] + sorted_list[indices[1]]) / 2
        pass
    else:
        indices.append(int(values / 2))

        median = sorted_list[indices[0]]
        pass

    return median, indices
    pass

median, median_indices = find_median(samples)
Q1, Q1_indices = find_median(samples[:median_indices[0]])
Q2, Q2_indices = find_median(samples[median_indices[-1] + 1:])

quartiles = [Q1, median, Q2]

print("(Q1, median, Q3): {}".format(quartiles))


