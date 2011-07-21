#!/usr/bin/python
"""
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest = 0
for i in range(999,99,-1):
	for j in range(i,99,-1):
		prod = i * j
		if prod > largest:
			prodstr = str(prod)
			if prodstr == prodstr[::-1]:
				largest = prod
				break
		else:
			break

print largest

