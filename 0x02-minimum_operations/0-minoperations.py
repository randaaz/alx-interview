#!/usr/bin/python3

""" Module for calculating the minimum number of operations """


def minOperations(n):
    """
    Calculate the minimum number of operations needed to
    get exactly n 'H' characters in a file.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
