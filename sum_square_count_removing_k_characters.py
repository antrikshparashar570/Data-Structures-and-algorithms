import heapq

def squareSumCharacters(s, k):
	d = {}
	for i in s:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1

	A = [-1*d[i] for i in d]

	heapq.heapify(A)

	while k > 0:
		if A[0] == 0:
			return "Not Possible"
		A[0] += 1
		heapq.heapify(A)
		k -= 1

	ans = 0
	for i in A:
		ans += i*i

	return abs(ans)

print(squareSumCharacters("abbccc", 2))