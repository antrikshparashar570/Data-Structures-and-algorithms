mat = [[1,2,3],[4,6,5],[4,2,1]]
k = 12

def paths(mat, m, n, dp, k):
	if m == 0 and n ==0 and mat[m][n] == k:
		return 1
	elif m < 0 or n < 0:
		return 0
	else:
		dp[m][n][k] = paths(mat, m-1, n, dp, k-mat[m][n]) + paths(mat, m, n-1, dp, k-mat[m][n])

	return dp[m][n][k]

def path_sum_k(mat, k):
	m = len(mat)
	n = len(mat[0])

	dp = [[[-1 for k in range(1000)] for j in range(n)] for i in range(m)]

	return paths(mat, m-1, n-1, dp, k)

print(path_sum_k(mat, k))