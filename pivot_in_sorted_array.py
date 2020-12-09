A = [5, 6, 7, 8, 9, 10, 1, 1, 2, 3] 
n = len(A)
l = 0
h = len(A)-1

while l <= h:
	mid = int((l+h)/2)

	if mid == 0 or A[mid] < A[mid-1]:
		pivot = mid
		break
	elif A[mid] > A[h]:
		l = mid+1
	else:
		h = mid-1

print(pivot)