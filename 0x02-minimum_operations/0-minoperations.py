#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to obtain n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain n H characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        Returns the minimum ops count. If unreachable, returns 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations

if __name__ == "__main__":
    # Example usage
    n1 = 4
    print("Min # of operations to reach {} char: {}".
          format(n1, minOperations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}".
          format(n2, minOperations(n2)))
