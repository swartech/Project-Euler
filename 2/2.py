def fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

n = 0
sum = 0
while fib(n) <= 4000000:
	if fib(n) % 2 == 0: 
		sum += fib(n)
	n += 1
print(sum)
