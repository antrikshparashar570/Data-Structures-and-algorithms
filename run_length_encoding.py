s = "wwwwaaaxx"

res = s[0]
count = 1

for i in range(1,len(s)):
	if s[i-1] == s[i]:
		count += 1
	else:
		res += str(count) + s[i]
		count = 1

res += str(count)

print(res)