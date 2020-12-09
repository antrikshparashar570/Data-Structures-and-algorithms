A = [2, 3, 3, 5, 3, 4, 1, 7] 
k = 8

def maxx_repeating(A, k):
	n = len(A)
	for i in range(n):
		index = A[i]
		A[index%k] += k

	maxx = A[0]
	for i in range(n):
		maxx = max(maxx, int(A[i]/k))

	return maxx

print(maxx_repeating(A, 8))