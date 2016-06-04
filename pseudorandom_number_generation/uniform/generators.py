# Generowanie liczb losowych o rozkładzie jednostajnym
from math import floor, ceil


def __linear_congruential_generator(a, m, seed, n, c=0):
    """ Returns sequence of uniformly distributed random numbers over (0,1) interval.
    :param a: the multiplier
    :param m: the modulus
    :param c: the increment
    :param seed: initial state of generator
    :param n: length of a generated sequence
    """
    sequence = []
    x = seed
    for i in range(0, n):
        x = (x * a + c) % m
        sequence.append((x / m))
    return sequence


def __frac(x):
    """ Returns fractional part of x.
    :param x: a number which fraction is returned
    :return fractional part of x
    """
    if x >= 0:
        return x - floor(x)
    else:
        return x - ceil(x)


def __combined_generator(sequence1, sequence2, sequence3):
    """ Function that combines outputs of three random number generators into one sequence over (0,1) interval."""
    if len(sequence1) != len(sequence2) or len(sequence1) != len(sequence3):
        raise ValueError('All arrays have to be the same length!')
    length = len(sequence1)
    return [__frac(sequence1[i] + sequence2[i] + sequence3[i]) for i in (0, length)]


def __wh(seed1, seed2, seed3, m1, m2, m3, a1, a2, a3, n):
    """ General Wichman-Hill formula."""
    s1 = __linear_congruential_generator(a1, m1, seed1, n)
    s2 = __linear_congruential_generator(a2, m2, seed2, n)
    s3 = __linear_congruential_generator(a3, m3, seed3, n)
    return __combined_generator(s1, s2, s3)


def randu(seed, n):
    """ Original version of RANDU generator."""
    a, m = 65539, 2 ** 31
    return __linear_congruential_generator(a, m, seed, n)


def randu_custom_1(seed, n):
    """ Modification of RANDU."""
    a, m = 65539, 2 ** 31 - 3
    return __linear_congruential_generator(a, m, seed, n)


def randu_custom_2(seed, n):
    """ Modification of RANDU."""
    a, m = 81077, 2 ** 31
    return __linear_congruential_generator(a, m, seed, n)


def randu_custom_3(seed, n):
    """ Modification of RANDU."""
    a, m = 65539, 2 ** 62 - 1
    return __linear_congruential_generator(a, m, seed, n)


def wichmann_hill(seed1, seed2, seed3, n):
    """ Original Wichmann-Hill algorithm. """
    m1, m2, m3 = 30269, 30307, 30323
    a1, a2, a3 = 171, 172, 170
    return __wh(seed1,seed2,seed3,m1, m2,m3,a1,a2,a3,n)


def wichmann_hill_custom_1(seed1, seed2, seed3, n):
    """ Modification of Wichmann-Hill algorithm."""
    m1, m2, m3 = 39343, 39367, 39373
    a1, a2, a3 = 123, 122, 121
    return __wh(seed1,seed2,seed3,m1, m2,m3,a1,a2,a3,n)


def wichmann_hill_custom_2(seed1, seed2, seed3, n):
    """ Modification of Wichmann-Hill algorithm."""
    m1, m2, m3 = 39343, 39367, 39373
    a1, a2, a3 = 123, 122, 121
    return __wh(seed1,seed2,seed3,m1, m2,m3,a1,a2,a3,n)
