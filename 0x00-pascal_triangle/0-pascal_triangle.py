#!/usr/bin/python3

    """
    Generate Pascal's Triangle up to the nth row and print it.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
    """
def generate_pascals_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row and return it as a list of lists of integers.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
    """
    pascals_triangle = []

    if n <= 0:
        return pascals_triangle

    for row_index in range(n):
        current_row = []

        for element_index in range(row_index + 1):
            if element_index == 0 or element_index == row_index:
                current_row.append(1)
            else:
                previous_row = pascals_triangle[row_index - 1]
                current_element = previous_row[element_index - 1] + previous_row[element_index]
                current_row.append(current_element)

        pascals_triangle.append(current_row)

    return pascals_triangle
