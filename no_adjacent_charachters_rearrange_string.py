class key:
	def __init__(self, char, freq):
		self.char = char
		self.freq = freq

def heapify(A, i):
	l = 2*i + 1
	r = 2*i + 2
	lar = i

	if l < len(A) and A[l].freq > A[i].freq:
		lar = l
	if r < len(A) and A[r].freq > A[lar].freq:
		lar = r

	if lar != i:
		A[lar], A[i] = A[i], A[lar]
		heapify(A, lar)

def noAdjacent(s):
	d = {}
	for i in s:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1

	A = []
	for i in d:
		A.append(key(i, d[i]))

	for i in range(len(A)):
		heapify(A, i)

	prev = key("#", -1)

	ans = ""
	while len(A)>0:
		k = A.pop(0)
		ans += k.char

		if prev.freq > 0:
			A.insert(0, prev)
			heapify(A, 0)

		k.freq -= 1
		prev = k

	if len(s) == len(ans):
		print(ans)
	else:
		print("Invalid string")

noAdjacent("aabbbbbcc")