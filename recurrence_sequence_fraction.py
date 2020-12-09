def recurr(num, den):
	res = ""
	h = {}

	rem = num%den

	while rem and rem not in h:
		h[rem] = len(res)
		rem = rem*10
		res += str(int(rem/den))
		rem = rem%den

	print(res)
	return res[h[rem]:]

print(recurr(50, 22))