st = "218765"
s = list(st)

n = len(s)

small = n-1

for i in range(n-2, -1, -1):
	if s[i] < s[i+1]:
		small = i
		break

s[small], s[n-1] = s[n-1], s[small]
print(s)

s = s[:small+1] + s[:small:-1]

print("".join(s))