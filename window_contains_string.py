def window(s):
	n = len(s)
	count = 0
	dis_count = len(set([x for x in s]))
	leng = 9999999
	curr_count = {}
	start = 0
	for i in range(n):
		if s[i] in curr_count:
			curr_count[s[i]] += 1
		else:
			curr_count[s[i]] = 1

		if curr_count[s[i]] == 1:
			count += 1

		if count == dis_count:
			while curr_count[s[start]] > 1:
				if curr_count[s[start]] > 1:
					curr_count[s[start]] -= 1
					start += 1
			min_len = i - start + 1
			leng = min(leng, min_len)

	return (s[start:start+leng], start, leng)

print(window("aabcbcdbca"))