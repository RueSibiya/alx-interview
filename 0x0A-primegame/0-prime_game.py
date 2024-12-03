#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""

def isWinner(x, nums):
    """Determines the winner of the prime number game."""
    if x <= 0 or not nums or x != len(nums):
        return None

    ben_score = 0
    maria_score = 0

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for n in nums:
        # Count the number of primes up to n
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    return None

def sieve_of_eratosthenes(limit):
    """Generates a list indicating prime numbers up to the limit."""
    sieve = [1] * (limit + 1)
    sieve[0], sieve[1] = 0, 0  # 0 and 1 are not prime numbers

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = 0
    return sieve
