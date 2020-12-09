M = [[0, 0, 1, 1, 0], [1, 0, 1, 1, 0],  [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]

n = 4
m = 5

def isSafe(M, x, y, visited):
	if x >=0 and x < n and y >= 0 and y < m and M[x][y] and not visited[x][y]:
		return True
	return False

def dfs(M, i, j, visited, count):
	row = [-1, -1, -1, 0, 0, 1, 1, 1]
	col = [-1, 0, 1, -1, 1, -1, 0, 1]

	visited[i][j] = 1
	for k in range(len(row)):
		if isSafe(M, i+row[k], j+col[k], visited):
			count[0] += 1
			dfs(M, i+row[k], j+col[k], visited, count)


def biggestRegion(M):
	visited = [[0 for j in range(m)] for i in range(n)]

	res = 0
	for i in range(n):
		for j in range(m):
			print(i, j)
			if M[i][j] and not visited[i][j]:
				count = [1]
				dfs(M, i, j, visited, count)
				res = max(res, count[0])

	return res

print(biggestRegion(M))