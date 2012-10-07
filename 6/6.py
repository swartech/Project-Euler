sumOfSquares = 0
squareOfSum = 0
sum = 0

for i in range(101):
	sum += i
	sumOfSquares += (i * i)
squareOfSum = sum * sum
print(squareOfSum - sumOfSquares) 	
