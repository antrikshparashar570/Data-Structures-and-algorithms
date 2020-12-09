A = [10, 5, 6, 3, 2, 20, 100, 80]

def waveForm(A):

	for i in range(0, len(A), 2):
		if i > 0 and A[i] < A[i-1]:
			A[i], A[i-1] = A[i-1], A[i]

		if i < len(A)-1 and A[i] < A[i+1]:
			A[i], A[i+1] = A[i+1], A[i]

	return A

print(waveForm(A))