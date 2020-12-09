def permutations(s, l, r, res):
	if l == r:
		res.append("".join(s))
	else:
		for i in range(l, r+1):
			s[l], s[i] = s[i], s[l]
			permutations(s, l+1, r, res)
			s[l], s[i] = s[i], s[l]

res = []
s = "ABC"
a = list(s)
permutations(a, 0, len(a)-1, res)
print(res)