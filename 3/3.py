#horribly inefficient, needs improving

def primeCheck(n):
	i = 0
	if n == 2:
		return True 
	for i in range(2, n, 2):
		if n % i == 0:
			return False
	return True

num = 0
largest = 0
limit = 600851475143
for num in range(1, limit):
	if primeCheck(num):
		if limit % num == 0:
			limit /= num
			largest = num
			print(num)
print(largest)
	
