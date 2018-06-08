import math
def polysum(n,s):
	a=s/(2*math.tan(math.pi/n))
	p=s*n
	print a,":",p
	return p+(a*p)/2
print polysum(6,10)
