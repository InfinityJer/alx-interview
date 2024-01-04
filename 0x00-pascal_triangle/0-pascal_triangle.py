#!/usr/bin/python3
'''Module to generate Pascal's Triangle integers'''


def pascal_triangle(n):
    '''
    Function to generate Pascal's Triangle integers.

        Parameters:
            n (int): The number of rows in Pascal's triangle.

        Returns:
            pascal_triangle (list): List of lists representing Pascal's Triangle.
    '''
    pascal_triangle = list()

    if n <= 0:
        return pascal_triangle

    # Add the first row with value 1.
    if n > 0:
        pascal_triangle.append([1])

    # Add the second row with values 1, 1.
    if n > 1:
        pascal_triangle.append([1, 1])

    # Generate the remaining rows.
    for x in range(3, n+1):
        # Initialize the row with zeros.
        pascal_triangle.append([0] * x)

        # Set the first and last element of the row to 1.
        pascal_triangle[x-1][0] = 1
        pascal_triangle[x-1][x-1] = 1

        # Calculate the middle numbers based on the previous row.
        for y in range(1, x-1):
            pascal_triangle[x-1][y] = \
                pascal_triangle[x-2][y-1] + pascal_triangle[x-2][y]

    return pascal_triangle
