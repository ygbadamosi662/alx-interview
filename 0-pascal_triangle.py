#!/usr/bin/python3
"""
    Define the Pascal Triangle function
"""
from typing import List


def pascal_triangle(n: int) -> List[List]:
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
    """
        1. while loop to check if the len of pascal == n
        2. Fetch the last list recently added to pascal
        3. create a dummy list (temp) to append to.
        4. add the first number and next number into the dummy
        and finally append 1 to dummy signifying end of that list.
        5. append dummy to pascal.
    """
    while len(pascal) != n:
        triangle = pascal[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        pascal.append(temp)

    return pascal

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(10))
