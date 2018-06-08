
#Paying Debt off in a Year

#Question 1


def CalAnnualBal(b,aIR,mPR):
	for i in range(12):
		b=b-(mPR*b)
		b=b+(b*aIR)/12
	return round(b,2)
print "Remaining balance: ",CalAnnualBal(5000,0.18,0.02)   



#Question 2


def min(b,a):
	def bal(b,a,m):
		for i in range(12):
			b=b-m
			b=b+(b*a)/12
		return b
	for i in range(int(round(b/120,0))*10,b,10):
		if bal(b,a,i)<=0:
			return i
print "Lowest Payment(multiples of 10): ",min(5000,0.18)  #Example


#Question 3

def bisec(b,a):
	def bal(b,a,m):
		for i in range(12):
			b=b-m
			b=b+(b*a)/12
		return b
	l=b/12
	u=(b*((1+a/12)**12))/12
	while (u-l)>1:
		mid=(l+u)/2
		if bal(b,a,mid)>0:
			l=mid
		else :
			u=mid
	return round(mid,2)
print "Lowest Payment: ",bisec(5000,0.18)    #Example
