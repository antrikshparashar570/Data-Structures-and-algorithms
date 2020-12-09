n = 5

def dec_to_bin(x):
	s = ""
	while (x) > 0:
		s = str(int(x%2)) + s
		x = int(x/2)

	return s

print(dec_to_bin(n))