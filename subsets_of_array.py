A = [1, 2, 2]

def subsetsUtil(A, subset, index, res):
	if subset not in res:
		res.append(list(subset))

	for i in range(index, len(A)):
		subset.append(A[i])
		subsetsUtil(A, subset, i+1, res)
		subset.pop()
	return

def subsets(A):
	res = []
	subset = []
	index = 0
	subsetsUtil(A, subset, index, res)

	return res

print(subsets(A))