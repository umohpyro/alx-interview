#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for outerLoop in range(n):
        # define the first row and fill first and last idx with 1
        nextLine = [0] * (outerLoop+1)
        nextLine[0] = 1
        nextLine[len(nextLine) - 1] = 1

        for innerLoop in range(1, outerLoop):
            if innerLoop > 0 and innerLoop < len(nextLine):
                a = pascal_triangle[outerLoop - 1][innerLoop]
                b = pascal_triangle[outerLoop - 1][innerLoop - 1]
                nextLine[innerLoop] = a + b

        pascal_triangle[outerLoop] = nextLine

    return pascal_triangle