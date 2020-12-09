A = [8, 3, 1, 2]

curr_sum = 0
for i in range(len(A)):
	curr_sum += i*A[i]

maxx = curr_sum
summ = sum(A)

for i in range(1, len(A)):
	curr_sum = curr_sum - (summ - A[i-1]) + A[i-1]*(len(A)-1) 
	maxx = max(maxx, curr_sum)

print(maxx)