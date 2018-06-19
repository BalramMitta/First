import math
import time


def isPrime(n):
	if n%2 == 0:
		return False
	else:
		for i in range(3,int(math.sqrt(n)+1),2):
			if i%n == 0:
				return False
	return True


def nextPrime(n):
	while True:
		if isPrime(n):
			return n
		else:
			n=n+1


def genPrimes():
	next = 2
	while True:
		yield next
		next=nextPrime(next+1)


for i in genPrimes():
	print(i)
	time.sleep(1)
