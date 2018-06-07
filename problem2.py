a=raw_input("enter string : ")
n=len(a)
count=0
for i in range(n-2):
	if a[i:i+3] == "bob" :
		count=count+1
print "Number of times bob occers is:",count
