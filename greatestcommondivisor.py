#Greatest Common Divisor (GCD) is the largest integer that evenly divides two numbers
#e.g. gcd(10, 5) is 5, (14, 21) is 7, (80, 30) is 10, (7, 15) is 1, (9, 0) is 9
#definition gcd(a, b) = a, if b = 0, gcd(b, a mod b), otherwise

def gcd(a, b):
	"""Return the greatest common divisor of a and b.  gcd(10, 5) is 5, (14, 21) is 7, (80, 30) is 10, (7, 15) is 1, (9, 0) is 9 """
	if b == 0:
		return a
	else:
		return gcd(b, a % b) #recursion
print(gcd(7,15))