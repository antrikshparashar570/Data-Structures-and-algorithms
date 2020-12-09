string = "geeksforgeeks"
mask = "mask"

def remove(string, mask):
	m = [0]*256
	for i in range(len(mask)):
		m[ord(mask[i])] = 1

	res = ""
	for j in range(len(string)):
		temp = string[j]
		if m[ord(temp)] == 0:
			res += string[j]

	return res

print(remove(string, mask))