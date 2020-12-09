A = [1, 3, 20, 4, 1, 0]

def peakElement(A):
	low = 0
	high = len(A)-1

	while low <= high:
		mid = int((low+high)/2)

		if mid == 0 or A[mid] >= A[mid-1] and mid == len(A)-1 or A[mid] >= A[mid+1]:
			return mid

		elif A[mid] > A[mid+1]:
			high = mid-1
		
		else:
			low = mid+1

print(peakElement(A))