#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            print('{:d}'.format(matrix[i][j]), end="")
            if j < m-1:
                print(" ", end="")
        print()
