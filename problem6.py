#!/usr/bin/python
"""
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def square_of_sums(n):
    return n*n * (n+1)*(n+1) / 4

def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1))/ 6

n = 100
print square_of_sums(n) - sum_of_squares(n)
