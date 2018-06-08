def isIn(a,s):
	p=len(s)/2
	if a==s[p]:
		return True
	elif a>s[p] and p!=0 and p!=len(s)-1:
		return isIn(a,s[p+1:])
	elif a<s[p] and p!=0:
		return isIn(a,s[:p])
	else:
		return False
print isIn('c','abcdefghijkl')
print isIn('a','abcdefghijkl')
print isIn('f','abcdefghijkl')
print isIn('l','abcdefghijkl')
print isIn('d','abcdefghijkl')
print isIn('j','abcdefghijkl')
print isIn('k','abcdefghijkl')
print isIn('z','abcdefghijkl')
	
