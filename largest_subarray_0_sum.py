A = [15, -2, 2, -8, 1, 7, 10, 13]

n = len(A)

h = {}
maxxlen = 0
curr_sum = 0
for i in range(n):

	curr_sum += A[i]
	
	if A[i] == 0 and maxxlen == 0:
		maxxlen = 1

	if curr_sum == 0:
		maxxlen = i+1

	if curr_sum in h:
		maxxlen = max(maxxlen, i - h[curr_sum])
	else:
		h[curr_sum] = i

print(maxxlen)