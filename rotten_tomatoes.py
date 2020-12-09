mat = [[ 2, 1, 0, 2, 1],[1, 0, 1, 2, 1],[ 1, 0, 0, 2, 1 ]]

def is_safe(m, n, i, j):
	if i >= 0 and i < m and j >= 0 and j < n:
		return True

def rotten(mat):
	m = len(mat)
	n = len(mat[0])
	q = []
	time = 0
	for i in range(m):
		for j in range(n):
			if mat[i][j] == 2:
				q.append((i, j))

	while len(q) > 0: 
		print(q)
		changed = False
		l = len(q)
		while l:
			ele_i, ele_j = q.pop(0)

			if is_safe(m, n, ele_i-1, ele_j) and mat[ele_i-1][ele_j] == 1:
				mat[ele_i-1][ele_j] = 2
				q.append((ele_i-1, ele_j))
				changed = True
			if is_safe(m, n, ele_i+1, ele_j) and mat[ele_i+1][ele_j] == 1:
				mat[ele_i+1][ele_j] = 2
				q.append((ele_i+1, ele_j))
				changed = True
			if is_safe(m, n, ele_i, ele_j-1) and mat[ele_i][ele_j-1] == 1:
				mat[ele_i][ele_j-1] = 2
				q.append((ele_i, ele_j-1))
				changed = True
			if is_safe(m, n, ele_i, ele_j+1) and mat[ele_i][ele_j+1] == 1:
				mat[ele_i][ele_j+1] = 2
				q.append((ele_i, ele_j+1))
				changed = True

			l -= 1

		if changed == True:
			time += 1

	return time

def check(mat):
	m = len(mat)
	n = len(mat[0])
	time = rotten(mat)
	for i in range(m):
		for j in range(n):
			if mat[i][j] == 1:
				return -1
	return time

print(check(mat))
