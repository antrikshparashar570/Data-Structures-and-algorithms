import heapq


A = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k = 3


h = []
for i in range(len(A)):
	A[i] = -1*A[i]
	if len(h) < k:
		heapq.heappush(h, A[i])
	elif abs(A[i]) >= abs(h[0]):
		continue
	else:
		heapq.heappushpop(h, A[i])

	heapq.heapify(h)

for i in h:
	print(i*-1, end=" ")