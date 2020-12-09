A = [5, 5, 5, 4, 4, 4, 6, 8, 8]

def sort(A):
	d = {}
	for i in range(len(A)):
		if A[i] in d:
			d[A[i]] += 1
		else:
			d[A[i]] = 1

	d = sorted(d.items(), key = lambda x: (x[0], x[1]))

	print(d)

sort(A)