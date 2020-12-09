s = "abbbccc"
k = 2

d = {}
for i in range(len(s)):
	if s[i] in d:
		d[s[i]] += 1
	else:
		d[s[i]] = 1

class character:
	def __init__(self, var, freq):
		self.var = var
		self.freq = freq

def heapify(A, i):
	maxx = i

	l = 2*i + 1
	r = 2*i + 2

	if l < len(A) and A[i].freq < A[l].freq:
		maxx = l

	if r < len(A) and A[maxx].freq < A[r].freq:
		maxx = r

	if maxx != i:
		A[maxx], A[i] = A[i], A[maxx]
		heapify(A, maxx)

li = []
for i in d.keys():
	li.append(character(i, d[i]))

for i in range(k-1, -1, -1):
	heapify(li, 0)
	li[0].freq -= 1
	print(li[i].var, li[i].freq)

ans = 0
for i in range(len(li)):
	ans += li[i].freq*li[i].freq

print(ans)
"""def heapsort(A):
	for i in range(int(len(A)/2)-1, -1, -1):
		heapify(A, i)

	#for i in range(len(A)-1, -1, -1):
	#	A[i], A[0] = A[0], A[i]
		heapify(A[1:], 0)
	return A"""

#print(heapsort(A))