def gcdRecur(a,b):
	if a%b==0:
		return b
	else:
		return gcdRecur(b,a%b)
print gcdRecur(12,15)
