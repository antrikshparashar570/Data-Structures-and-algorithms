import math

x = 9
p = 2

def sqrt(x):
	l = 2
	h = x
	ans = 0

	while l < h:
		mid = int((l+h)/2)
		if mid*mid == x:
			return mid
		elif mid*mid > x:
			h = mid - 1
		else:
			l = mid + 1
			ans = mid

	for i in range(p):
		j = 1/math.pow(10, i+1)
		while ans*ans <= x:
			ans = ans + j
		ans = ans - j

	return ans

print(sqrt(x))