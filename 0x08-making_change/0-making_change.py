#!/usr/bin/python3
"""
Module for making change with minimum number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
        
    # Initialize remaining total
    rem = total
    
    # Initialize count of coins used
    coins_count = 0
    
    # Initialize index for iterating through sorted coins
    coin_idx = 0
    
    # Sort coins in descending order
    sorted_coins = sorted(coins, reverse=True)
    
    # Get the length of the coins list
    n = len(coins)
    
    # Loop until remaining total is greater than 0
    while rem > 0:
        # If exhausted all coins and still have remaining total, return -1
        if coin_idx >= n:
            return -1
            
        # If the current coin can be used to reduce the remaining total
        if rem - sorted_coins[coin_idx] >= 0:
            # Reduce the remaining total
            rem -= sorted_coins[coin_idx]
            
            # Increment the count of coins used
            coins_count += 1
        else:
            # Move to the next coin
            coin_idx += 1
            
    # Return the count of coins used to meet the total
    return coins_count
