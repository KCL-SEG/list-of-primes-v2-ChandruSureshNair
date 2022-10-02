"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    n = 2
    while len(list) < number_of_primes:
        factors = False
        i = 2
        while not factors and i < n:
            factors = n % i == 0
            i += 1
        if not factors:
            list.append(n)
        n += 1

    return list
