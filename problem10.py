#!/usr/bin/python
"""
Problem 10
08 February 2002

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
def generate_primes(max):
	candidates = []
	[candidates.append((i,True)) for i in range(0,max)]
	for i in range(4,max,2):
		candidates[i] = (i,False)
	for i in range(3,max,2):
		for j in range(i + i, max, i):
			candidates[j] = (j,False)

	return [i for (i,prime) in candidates if prime == True]


print sum(generate_primes(2000000)[2:])
