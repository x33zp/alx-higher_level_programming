#!/usr/bin/python3
"""finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """the function that finds the peak
    """
    listSize = len(list_of_integers)

    if listSize == 0:
        return None
    elif listSize == 1:
        return list_of_integers[0]
    elif listSize == 2:
        return max(list_of_integers)

    mid = listSize//2
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
