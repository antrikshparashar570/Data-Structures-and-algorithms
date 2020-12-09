A = [1, 3, 0, 2, 5]

def prevSmall(A):
	s = []

	for i in range(len(A)):

		while len(s)>0 and A[i] <= s[-1]:
			s.pop()

		if len(s) == 0:
			print(A[i], -1)
		else:
			print(A[i], s[-1])

		s.append(A[i])


prevSmall(A)