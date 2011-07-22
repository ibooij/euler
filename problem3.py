#!/usr/bin/python
"""
Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def next_prime(n):
	for p in range(3, int(math.sqrt(n))):
		if n % p == 0:
			yield p

def product(l):
	p = 1
	for i in l:
		p *= i
	return p

import math
def find_prime_factors(n):
	prime_gen = next_prime(n)
	primes = []
	while product(primes) != n:
		primes.append(prime_gen.next())
	return primes[-1]

print find_prime_factors(600851475143)
