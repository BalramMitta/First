a=raw_input("enter string : ")
n=len(a)
v="aeiou"
count=0
for i in range(n):
	if a[i] in v:
		count=count+1
print "Number of vowels:",count
