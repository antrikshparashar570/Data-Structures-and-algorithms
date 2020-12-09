import sys

arr = [1, 3, 6, 1, 0, 9]

def minJumps(A):
	jumps = [0 for i in range(len(A))]

	n = len(A)
	for i in range(1, n):
		jumps[i] = sys.maxsize
		for j in range(i):
			if i <= j+A[j] and jumps[j] != sys.maxsize:
				jumps[i] = min(jumps[i], jumps[j]+1)
				break
	return jumps[n-1]

print(minJumps(arr))