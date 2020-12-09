s = [30, -5, 18, 14, -3]

def sort_insert(s, ele):
	if len(s) == 0 or s[-1] < ele:
		s.append(ele)
	else:
		temp = s.pop()
		sort_insert(s, ele)
		s.append(temp)

def sort(s):
	if len(s) != 0:
		temp = s.pop()
		sort(s)
		sort_insert(s, temp)

sort(s)
print(s)