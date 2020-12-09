import math

def countBst(n):

	T = [0 for i in range(n+1)]
	Tr = [0 for i in range(n+1)]

	T[0] = 1
	T[1] = 1

	for i in range(2, n+1):
		for j in range(i):

			T[i] += T[j]*T[i-j-1]
		Tr[i] += T[i]*math.factorial(i)

	return (T[n], Tr[n])

print(countBst(5))