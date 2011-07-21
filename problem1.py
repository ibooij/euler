#!/usr/bin/python
"""
Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def natural_numbers_below_which_are_multiple_of_3_or_5(n):
	return [i for i in range(1,n) if i % 3 == 0 or i % 5 == 0]

print sum(natural_numbers_below_which_are_multiple_of_3_or_5(1000))
