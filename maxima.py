A = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]

def maxima(A):
	n = len(A)

	if n == 1:
		return A[0]
	l = 0
	h = n-1

	while l <= h:
		mid = int((l+h)/2)
		if mid == 0 or (A[mid] > A[mid-1] and A[mid] > A[mid+1]) or mid == n-1:
			return mid
		elif A[mid] > A[mid+1]:
			h = mid-1
		else:
			l = mid+1

	return -1

print(maxima(A))