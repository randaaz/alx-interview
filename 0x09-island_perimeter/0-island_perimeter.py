#!/usr/bin/python3

""" Module for calculating the perimeter of an island in a grid. """


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in the grid.
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in idx]

            if grid[i][j]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idx)])

    return (count)
