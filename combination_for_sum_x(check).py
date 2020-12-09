A = [2, 4, 6, 8]
x = 8

def combinations(A, x, ans, i, res):
	if x < 0:
		return

	if x == 0:
		print(ans)
		res.append(list(ans))
		return

	while i < len(A) and x - A[i] >= 0:

		ans.append(A[i])
		combinations(A, x-A[i], ans, i, res)
		i += 1

		ans.pop()

res = []
ans = []
combinations(A, x, ans, 0, res)

print(res)