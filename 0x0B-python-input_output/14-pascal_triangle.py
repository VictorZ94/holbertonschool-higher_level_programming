#!/usr/bin/python3
"""Doc
"""


def pascal_triangle(n):
    """pascal's trinagule """
    if n <= 0:
        return []
    lisTri = [[1]]
    for i in range(2, n+1):
        tmp = [0] + lisTri[i-2] + [0]
        lisTri.append([sum(par) for par in zip(tmp, tmp[1:])])
    return lisTri
