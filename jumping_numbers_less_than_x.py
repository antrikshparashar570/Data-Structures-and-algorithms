x = 470

def jump_num(x, i, ans):
	q = []
	q.append(i)

	while len(q) > 0:
		num = q.pop()
		if num <= x:
			ans.append(num)
			last_digit = num%10

			if last_digit == 0:
				q.append(num*10 + last_digit + 1)
			elif last_digit == 9:
				q.append(num*10 + last_digit - 1)
			else:
				q.append(num*10 + last_digit + 1)
				q.append(num*10 + last_digit - 1)

def jumping_num(x):
	ans = []
	for i in range(1, 10):
		jump_num(x, i, ans)
	return ans

print(jumping_num(x))