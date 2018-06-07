a=raw_input("enter string : ")
n=len(a)
count=0
max1=0
i=0
for i in range(n-1):
	if a[i] <= a[i+1] :
		count=count+1
	else :
		if max1 < count :
			max1=count
			l_ind=i-max1
			u_ind=i+1
		count=0
if max1 < count :
			max1=count
			l_ind=i-max1-1
			u_ind=i+1
print "Longest substring in alphabetical order is:",a[l_ind:u_ind]
