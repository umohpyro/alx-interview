#!/usr/bin/python3
"""pascal's triangle generator"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    # return (first row n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        buffer = []

        for j in range(i+1):
            if j == 0 or j == i:
                buffer.append(1)
            else:
                buffer.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(buffer)
    # print(triangle)
    return triangle
