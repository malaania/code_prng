# Funkcje wspomagające przeprowadzenie testu chi-kwadrat
from math import ceil, floor


def goodness_of_fit(expected, observed):
    """Returns value of chi-square statistics.
    :param expected: array of expected values
    :param observed: array of observed values
    :return chi-square statistics
    """
    if len(expected) != len(observed):
        raise ValueError('Expected and observed arrays have to be the same length!')
    length = len(expected)
    sum = 0
    for i in range(0, length):
        sum += (observed[i] - expected[i]) ** 2 / expected[i]
    return sum

# todo: adjust function to make it more generic
def make_bins(sequence):
    max_val = ceil(max(sequence))
    buckets = [0] * max_val
    for s in sequence:
        buckets[floor(s)]+=1
    return buckets