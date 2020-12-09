def divideUtil(func):
	def inner(a, b):
		print("asdad")
		if b == 0:
			print("Error")
			return

		return func(a, b)
	return inner

@divideUtil
def divide(a, b):
	print(a/b)

divide(4,2)