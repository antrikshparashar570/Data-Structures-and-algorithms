A = [1, 101, 2, 3, 100, 4, 5]

n = len(A)
m = [A[i] for i in range(n)]
#count = [1 for i in range(n)]

for i in range(n-1):
	for j in range(i+1, n):
		if A[j] > A[i] and m[i] + A[j] > m[j]: #and count[i] + 1 > count[j]:
			m[j] = m[i] + A[j]
			#count[j] = count[i] + 1
	print(m)
	#print(count)

print(max(m))
#print(max(count))