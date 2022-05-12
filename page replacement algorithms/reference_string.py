'''
Eduardo Sosa
April 20th, 2022
CS337 - Project 08
reference_string.py
'''


import random
from numpy.random import choice


# Generate a nonlocality string of a given length and with
# An upper limit to the number of unique pages. If None, then
# The number of unique pages is bounded by length.
def nonlocality_string(length, limit=None):
    if not limit:
        limit = length
    return [random.randint(1, limit) for ind in range(length)]


# Generate a locality string that picks a page based on its own
# Index and then add or subtract a random number within a range.
def locality_string(length):
    res_list = []
    ind = 0
    while len(res_list) < length:
        page = random.randint(-10, 10) + ind
        if 0 < page < length:
            res_list.append(page)
            ind += 1
    return res_list


# Generate a reference string with weighted probabilities of size length.
def probability_string(length):
    res_list = [i for i in range(10)]
    weight = [0.01, 0.01, 0.40, 0.20, 0.10, 0.08, 0.01, 0.01, 0.08, 0.10]
    res_weighted = choice(
        res_list, length, p=weight)

    return res_weighted
