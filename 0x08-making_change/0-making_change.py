#!/usr/bin/python3
"""
Module for making change with minimum number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total < 1:
        return 0

    # Initialize a list to store minimum number of coins for each total
    min_coins = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    min_coins[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the min_coins list for each total from coin value to total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If min_coins[total] remains float('inf'), it means total cannot be met
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]


# Testing the function
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
