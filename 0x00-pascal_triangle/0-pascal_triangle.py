#!/usr/bin/python3

    """
    Generate Pascal's Triangle up to the nth row and print it.

    Args:
    - n: An integer representing the number of rows in Pascal's Triangle.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
    """

def pascal_triangle(n):
    '''
    creates a list of lists of integers representing the
    Pascal's triangle of a given integer and prints it
    '''
    pt = []
    if type(n) is not int or n <= 0:
        return pt

    for x in range(n):
        ct = []
        for y in range(x+1):
            if y == 0 or y == x:
                ct.append(1)
            else:
                ct.append(pt[x-1][y] + pt[x-1][y-1])
        pt.append(ct)

        # Print the current row
        print("[{}]".format(",".join(map(str, ct)))

    return pt
