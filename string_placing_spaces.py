string = "ABCD"

def patternUtil(string, buff, i, j, n):
	if i == n:
		buff[j] = ""
		print("".join(buff))
		return 

	buff[j] = string[i]
	patternUtil(string, buff, i+1, j+1, n)

	buff[j] = " "
	buff[j+1] = string[i]

	patternUtil(string, buff, i+1, j+2, n)

def pattern(string):
	buff = ["" for i in range(len(string)*2)]
	n = len(string)
	buff[0] = string[0]

	patternUtil(string, buff, 1, 1, n)


pattern(string)