
import operator
import sys

for a in range(1, 300):
	for b in range(a, 1000 - 2 * a + 1):
		c = 1000 - a - b
		if c > b and a*a + b*b == c*c:
			print reduce(operator.mul, [a,b,c], 1)
			sys.exit(0)


