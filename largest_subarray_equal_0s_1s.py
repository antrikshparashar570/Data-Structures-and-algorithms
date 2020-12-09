A = [1, 0, 0, 1, 0, 1, 1]

def lar_subarray(A):
	n = len(A)
	d = {}
	maxx = 0
	summ = 0
	start = 0
	end = 0

	for i in range(n):
		if A[i] == 0:
			A[i] = -1

	for i in range(n):
		summ = summ + A[i]

		if summ == 0:
			maxx = i+1
			end = i
		if summ in d:
			if maxx < i - d[summ]:
				start = d[summ]+1
				end = i
		else:
			d[summ] = i

	print(start, end)

lar_subarray(A)
