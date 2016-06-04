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
    statistics = 0
    for i in range(0, length):
        statistics += (observed[i] - expected[i]) ** 2 / expected[i]
    return statistics

# todo: adjust function to make it more generic
def make_bins(sequence):
    max_val = ceil(max(sequence))
    buckets = [0] * max_val
    for s in sequence:
        buckets[floor(s)]+=1
    return buckets

def __linear_transform(a, b, x):
    return a*x + b

def make_bins_continuous(interval, bin_size, generated_sequence, minus_inf=0, plus_inf = 0):
    """
    :param minus_inf: takes values from {0,1}, where zero means not taking into account values smaller than interval[0]
    :param plus_inf: takes values from {0,1}, where zero means not taking into account values bigger than interval[1]
    """
    if minus_inf != 0:
        minus_inf = 1
    if plus_inf != 0:
        plus_inf = 1
    # linear transformation of interval bins to array indexing y=ax+b
    a = 1/bin_size
    b = -1*interval[0]*a
    #number of bins
    n= int((interval[1]-interval[0])/bin_size)
    max_index = n + minus_inf + plus_inf
    bins = [0]*(max_index)
    for x in generated_sequence:
        y = __linear_transform(a,b,x)
        index = floor(y) + minus_inf
        if x < interval[0] and minus_inf == 1:
            bins[0]+=1
        elif index < max_index and index >= 0:
            bins[index]+=1
        elif plus_inf == 1 and x > interval[1]:
            bins[max_index-1]+=1
    return bins





