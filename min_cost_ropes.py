import heapq
A = [4, 3, 2, 6]

def min_cost(A):
	cost = 0
	sum = 0
	heapq.heapify(A)
	while len(A) > 1:
		min1 = heapq.heappop(A)
		min2 = heapq.heappop(A)
		sum = min1 + min2
		heapq.heappush(A, sum)
		cost += sum

	return cost

print(min_cost(A))