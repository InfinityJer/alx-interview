#!/usr/bin/python3
"""
Module for Minimum Operations problem
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to 
        result in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.

    """
    if n <= 1:
        return 0

    # Create a list to store the minimum number of operations for each index
    dp = [float('inf')] * (n + 1)

    # Base case: it takes 0 operations to have 1 'H'
    dp[1] = 0

    # Iterate through each number and calculate the minimum operations needed
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: 
           {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: 
           {}".format(n, minOperations(n)))
