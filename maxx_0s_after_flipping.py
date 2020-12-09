A = [1, 0, 1, 0, 1, 1, 0]

count_0 = 0
summ = 0
maxx = 0

for i in range(len(A)):
	if A[i] == 0:
		count_0 += 1
		A[i] = -1

	summ += A[i]
	if summ <= 0:
		maxx = max(maxx, summ)
		summ = 0

	maxx = max(maxx, summ)
print(maxx + count_0)