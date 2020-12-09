A = [1, -2, -3, 0, 7, -8, -2]

def max_subarr_pro(A):
	max_so_far = 0

	max_end_here = 1
	min_end_here = 1
	flag = 0

	for i in range(len(A)):
		if A[i] > 0:
			max_end_here = max_end_here*A[i]
			min_end_here = min(min_end_here*A[i], 1)
			flag = 1
		elif A[i] == 0:
			max_end_here = 1
			min_end_here = 1
		else:
			temp = max_end_here
			max_end_here = max(min_end_here*A[i], 1)
			min_end_here = temp*A[i]

		max_so_far = max(max_so_far, max_end_here)

	if flag == 0 and max_so_far == 1:
		return 0
	return max_so_far

print(max_subarr_pro(A))