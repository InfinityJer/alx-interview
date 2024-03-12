#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(limit):
    """Generate all prime numbers up to a given limit using Sieve of Eratosthenes algorithm."""
    primes = []
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

def can_make_move(nums):
    """Check if there are any prime numbers left to make a move."""
    for num in nums:
        if is_prime(num):
            return True
    return False

def isWinner(x, nums):
    """Determine the winner of the game for each round."""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if can_make_move(range(1, n + 1)):
            # Maria always starts, so if the number is even, Ben wins
            if n % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1
    # Compare the number of wins for Maria and Ben
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test
print("Winner:", isWinner(3, [4, 5, 1]))  # Output should be "Ben"
