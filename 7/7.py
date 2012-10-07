def primeCheck(n):
	i = 0
	if n < 4:
		return True 
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

n = 0
primes = 0
while primes <= 10001:
	n += 1
	if primeCheck(n) == True:
		primes += 1
print(n)
	
