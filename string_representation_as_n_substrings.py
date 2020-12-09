def lpsArray(string, n, lps):
	l = 0
	i = 1

	while i < n:
		if string[i] == string[l]:
			l += 1
			lps[i] = l
			i += 1

		else:
			if l != 0:
				l = lps[l-1]

			else:
				lps[i] = 0
				i += 1

def part_substring(string):
	n = len(string)
	lps = [0 for i in range(n)]

	lpsArray(string, n, lps)

	l = lps[n-1]

	if l > 0 and n%(n-l) == 0:
		return True
	else:
		return False

print(part_substring("abcdababcdab"))