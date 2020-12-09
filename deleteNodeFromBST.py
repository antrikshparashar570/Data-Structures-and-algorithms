def minValNode(A):
	curr = A

	while curr.left:
		curr = curr.left

	return curr

def delete(A, node):

	if A is None:
		return A

	elif node.val < A.val:
		A.left = delete(A.left, node)

	elif node.val > A.val:
		A.right = delete(A.right, node)

	else:
		if A.left is None:
			temp = A.right
			A = None
			return temp

		elif A.right is None:
			temp = A.left
			A = None
			return temp

		temp = minValNode(A.right)

		A.val = temp.val

		A.right = delete(A.right, temp.val)