satisfied = False
n = 0
factorCount = 0
while not satisfied:
	factorCount = 0
	n += 2520
	for i in range(1, 20):
		if n % i == 0:
			factorCount += 1
			if factorCount == 19:
				satisfied = True
print(n)
