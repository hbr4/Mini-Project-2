from collections import Counter

def mode(num):
    values = len(num)
    data = Counter(num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

    if len(mode) == values:
        get_mode = "No mode found"
    else:
        get_mode = mode[0]

    return get_mode
