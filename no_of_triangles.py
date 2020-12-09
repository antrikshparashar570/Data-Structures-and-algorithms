A = [4, 3, 5, 7, 6]

def triangles(A):
	A.sort()

	ans = 0
	for i in range(2, len(A)):
		j = 0
		k = i-1

		while j < k:
			if A[j] + A[k] > A[i]:
				ans += k-j
				k -= 1
			else:
				j += 1

	print(ans)

triangles(A)