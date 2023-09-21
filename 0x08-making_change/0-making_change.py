#!/usr/bin/python3
"""
    This function solves the coin change programming problem using bottom-top
    brute forcing algorithm.
"""


def makeChange(coins, total):
    """
    Using brute force to find the minimum coins required to get the total
    cost.

    Args:
    coins[list]: list of all possible coins that can be used in this
    program.
    total: total cost
    """
    if total <= 0:
        return 0

    dp = [1 + total] * (total + 1)
    dp[0] = 0

    for var in range(1, total + 1):
        for coin in sorted(coins):
            if var - coin == 0:
                dp[var] = min(dp[var], dp[var - coin] + 1)
                break
            if var - coin > 0:
                dp[var] = min(dp[var], dp[var - coin] + 1)

    return dp[total] if dp[total] != (total + 1) else -1
