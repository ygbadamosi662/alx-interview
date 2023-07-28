#!/usr/bin/python3
"""
    Defines the pascal_triangle function
"""


def pascal_triangle(n):
    """
        Represents pascal triangle of n

        Args:
            n (_type_): Integer
        Returns:
            List[List]
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) < n:
        prev_row = pascal[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        pascal.append(new_row)

    return pascal
