def flipped(A, B):
	n = A^B
	count = 0
	m = 1
	while n > 0:
		if n&m != 0:
			count += 1
		n = n >> 1

	print(count)

flipped(7, 10)