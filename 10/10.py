import math

limit = 2000000

L = list(True for i in range(limit))
L[0] = False
L[1] = False
sum = 0

for i in range(2, int(math.sqrt(limit) + 1)):
	if L[i] is True:
		for j in range (i * i, limit, i):
			L[j] = False

for k in range (limit):
	if L[k] is True:
		sum += k
print(sum)
