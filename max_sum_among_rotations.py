A = [8, 3, 1, 2]

def maxSum(A):
	summ = sum(A)
	index_sum = 0
	for i, a in enumerate(A):
		index_sum += a*i

	res = index_sum
	for i in range(1, len(A)):
		index_sum = index_sum - (summ-A[i-1]) + A[i-1]*(len(A)-1)

		res = max(res, index_sum)

	return res

print(maxSum(A))