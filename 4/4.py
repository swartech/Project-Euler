def palindromeCheck(n):
	li = [int(char) for char in str(n)]
	li2 = li[::-1]
	if li == li2:
		return True
	return False

solution = 0
for i in range(999):
	for j in range(999):
		product = i * j
		if palindromeCheck(product):
			if product > solution:
				solution = product
print(solution)
