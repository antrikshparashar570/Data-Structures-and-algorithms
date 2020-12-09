A = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]

d ={}
curr_max = 0
s = set()

for i in range(len(A)-1):
	for j in range(i+1, len(A)):
		if A[i][0] == A[j][0]:
			slope = "inf"
		else:
			slope = float(A[j][1]-A[i][1])/float(A[j][0]-A[i][0])

		print(A[i], A[j], slope)
		if slope not in d:
			d[slope] = set()

		d[slope].add(A[i])
		d[slope].add(A[j])

		curr_max = max(len(d[slope]), curr_max)

print(curr_max)