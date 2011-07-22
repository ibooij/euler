#!/usr/bin/python
"""
Problem 7
28 December 2001

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math

def is_prime(n, primes):
    if n < 2:
        return False
    
    max = math.ceil(math.sqrt(n))
    for p in primes:
        if n % p == 0:
            return False

    return True

def n_th_prime(n):
    primes = [2,3]
    i = 5
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2

    if len(primes) % 20 == 0:
        print len(primes)
    return primes

print n_th_prime(10001)[-1]
    
                    
