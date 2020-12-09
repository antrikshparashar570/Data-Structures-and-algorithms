A = [(4, 6), (6, 5), (7, 3),(4, 5)]
#A = [(6, 4), (3, 8), (4, 3), (5, 4)]

def tour(A):

	a = 0
	b = 0
	for i in range(len(A)):
		a += A[i][0]
		b += A[i][1]

	if a >= b:
		s=0
		index=0
		for i in range(len(A)):
			if A[i][0]+s>=A[i][1]:
				s=A[i][0]+s-A[i][1]
			else:
				s=0
				index=i+1
		return index
	else:
		return -1


print(tour(A))