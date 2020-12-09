def insertions(s):
	n = len(s)
	dp = [[0 for j in range(n)] for i in range(n)]

	for gap in range(1, n):
		l = 0
		for h in range(gap, n):
			if s[l] == s[h]:
				dp[l][h] = dp[l+1][h-1]

			else:
				dp[l][h] = min(dp[l+1][h], dp[l][h-1]) + 1

			l += 1

	print(dp[0][n-1])


insertions("geeks")