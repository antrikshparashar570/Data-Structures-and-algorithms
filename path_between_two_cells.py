Mat = [[0, 3, 0, 3], [3, 0, 3, 3], [1, 3, 3, 0], [0, 3, 3, 2]]
n = 4
m = 4

def isSafe(M, i, j, visited):
	a = [1, 2, 3]
	if i >= 0 and i < n and j >= 0 and j < m and M[i][j] in a  and not visited[i][j]:
		return True
	return False

def dfs(M, i, j, visited):
	if isSafe(M, i, j, visited):
		visited[i][j] = 1
		if M[i][j] == 2:
			return True
		return dfs(M, i-1, j, visited) or dfs(M, i, j+1, visited) or dfs(M, i+1, j, visited) or dfs(M, i, j-1, visited)
	return False

def path(M):
	visited = [[0 for j in range(m)] for i in range(n)]
	for i in range(n):
		for j in range(m):
			if M[i][j] == 1:
				return dfs(M, i, j, visited)

print(path(Mat))