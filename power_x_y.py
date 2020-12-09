import math

n = 343

def x_y(n):
	for i in range(2, int(math.sqrt(n))+1):
		temp = n
		while temp > 0:
			if temp%i == 0:
				temp = int(temp/i)
				print(temp)
			else:
				break

		if temp == 1:
			return True

	return False

print(x_y(n))