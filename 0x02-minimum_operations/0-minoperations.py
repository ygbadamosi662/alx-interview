"""
"""
from functools import reduce
import math


def minOperations(n):
    """
        Returns a integer of the minimum operation that can occur.

    Args:
        n (integer): the number of times an operation is made to reach this
        integer.
    """
    if n == 1:
        return 0

    ops = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        ops = ops + n

    return ops
