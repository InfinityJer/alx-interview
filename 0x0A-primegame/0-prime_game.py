#!/usr/bin/python3
"""This module contains functions determining the winner of a prime game session."""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    
    Args:
        x (int): The number of rounds to play.
        nums (list): List of integers representing the game rounds.

    Returns:
        str or None: Name of winner ('Maria' or 'Ben'), or None if the winner not determined.
    """
    # If the number of rounds is less than 1 or nums is empty, return None
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # Generate a list of primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    # Use Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    # Determine the winner based on the number of wins
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
