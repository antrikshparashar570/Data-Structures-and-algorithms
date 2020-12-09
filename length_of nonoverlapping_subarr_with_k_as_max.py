A = [4, 5, 7, 1, 2, 9, 8, 4, 3, 1]
k = 4

count = 0
flag = 0
ans = 0

for i in range(len(A)):
	if A[i] <= k:
		count += 1
		if A[i] == 4:
			flag = 1
	else:
		flag = 0
		count = 0

	if flag == 1:
		ans += count
		count = 0

	print(count, ans, flag)

print(ans)