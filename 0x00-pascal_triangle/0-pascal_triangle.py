#!/usr/bin/python3

    """
    Generate Pascal's Triangle up to the nth row and print it.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
    """
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    # Print the generated triangle
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

    return triangle

