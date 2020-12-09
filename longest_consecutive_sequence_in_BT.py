class newNode: 
    def __init__(self, data): 
        self.val = data  
        self.left = self.right = None

root = newNode(6)  
root.right = newNode(9)  
root.right.left = newNode(7)  
root.right.right = newNode(10)  
root.right.right.right = newNode(11)

A = root

def consec(root, length, parentvalplusone, res):
	if root is None:
		return 0

	if root.val == parentvalplusone:
		length += 1
	else:
		length = 1

	res[0] = max(res[0], length)

	consec(root.left, length, root.val+1, res)
	consec(root.right, length, root.val+1, res)

def consecutive(A):
	if A is None:
		return 0
	res = [0]
	consec(A, 0, A.val, res)

	return res[0]

print(consecutive(A))