A = [5, 4, 3, 2, 1]

p = [1 for i in range(len(A))]

for i in range(1, len(A)):
	p[i] = A[i-1]*p[i-1]
print(p)

P = 1

for i in range(len(A)-2, -1, -1):
	p[i] = p[i]*P
	P = P*A[i]

print(p)