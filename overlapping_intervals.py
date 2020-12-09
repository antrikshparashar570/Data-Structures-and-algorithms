A = [[8, 9], [2, 4], [4, 7]]

def intervals(A):

	A = sorted(A, key = lambda x:x[0])
	maxx = -1
	start = -1
	m = []
	for i in range(len(A)):
		if A[i][0] > maxx:
			if i != 0:
				m.append([start, maxx])
			start = A[i][0]
			maxx = A[i][1]
		else:
			if A[i][1] >= maxx:
				maxx = A[i][1]

	if [start, maxx] not in m:
		m.append([start, maxx])

	return m

print(intervals(A))