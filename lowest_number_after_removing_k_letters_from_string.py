def lowest(string, k, res):
	if k == 0:
		res += string
		print(res)
		return

	if k >= len(string):
		return

	minIndex = 0
	for i in range(len(string)):
		if string[i] < string[minIndex]:
			minIndex = i

	res += string[minIndex]

	new_str = string[minIndex:len(string)]

	lowest(new_str, k-minIndex, res)

def buildLowest(string, k):
	res = ""
	lowest(string, k, res)

buildLowest("121198", 2)