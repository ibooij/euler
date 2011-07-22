#!/usr/bin/python
"""
Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import operator
import sys

for a in range(1, 300):
	for b in range(a, 1000 - 2 * a + 1):
		c = 1000 - a - b
		if c > b and a*a + b*b == c*c:
			print reduce(operator.mul, [a,b,c], 1)
			sys.exit(0)


