import sys

def eggDrop(n, k):
	eggdp = [[0 for j in range(k+1)] for i in range(n+1)]

	for i in range(1, n+1):
		eggdp[i][1] = 1

	for j in range(1, k+1):
		eggdp[1][j] = j

	for i in range(2, n+1):
		for j in range(2, k+1):
			eggdp[i][j] = sys.maxsize
			for x in range(1, j+1):
				res = 1 + max(eggdp[i-1][x-1], eggdp[i][j-x])
				eggdp[i][j] = min(res, eggdp[i][j])

	return eggdp[n][k]

print(eggDrop(2, 36))