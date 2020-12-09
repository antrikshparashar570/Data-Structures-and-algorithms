import sys

A = [9, 6, 5, 1]
V = 11

def coins(A,  V):
	table  = [0 for i in range(V+1)]

	table[0] = 0
	for i in range(1, V+1):
		table[i] = sys.maxsize

	for i in range(len(A)):
		for j in range(1, V+1):
			if A[i] <= j:
				res = table[j - A[i]]
				if res != sys.maxsize:
					table[j] = min(res + 1, table[j])

	return table[V]

print(coins(A, V))