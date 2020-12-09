#A = [7, 6, 5, 4, 3, 2, 1]
A = [12, 1, 78, 90, 57, 89, 56]
k = 3

def max(A, k):
	ans = []
	q = []
	maxx = 0
	for i in range(k):
		while len(q) > 0 and A[q[-1]] <= A[i]:
			q.pop()
		q.append(i)

	ans.append(A[q[0]])

	for i in range(k, len(A)):
		while len(q) > 0 and q[0] <= i-k:
			print(q[0], i-k)
			q.pop(0)

		while len(q) > 0 and A[q[-1]] <= A[i]:
			q.pop()

		q.append(i)
		ans.append(A[q[0]])

	return ans

print(max(A, k))