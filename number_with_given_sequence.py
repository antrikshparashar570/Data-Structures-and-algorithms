def number(seq):
	ans = ""
	s = []
	for i in range(len(seq)+1):
		s.append(i+1)
		if i == len(seq) or seq[i] == "I":
			while len(s) > 0:
				ans += str(s.pop())

	return ans

print(number("IDID"))