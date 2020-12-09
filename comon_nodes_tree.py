class node:  
      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.val = data

A = node(5)
A.left = node(1)
A.right = node(10)
A.left.left = node(0)
A.left.right = node(4)
A.right.left = node(7)
A.right.left.right = node(9)

B = node(10)
B.left = node(7)
B.right = node(20)
B.left.left = node(4)
B.left.right = node(9)

def common_nodes(root1, root2):
	s1 = []
	s2 = []

	while 1:
		if root1:
			s1.append(root1)
			root1 = root1.left
		elif root2:
			s2.append(root2)
			root2 = root2.left

		elif len(s1) != 0 and len(s2) != 0:
			root1 = s1[-1]
			root2 = s2[-1]

			if root1.val == root2.val:
				print(root1.val, " ")
				s1.pop()
				s2.pop()
				root1 = root1.right
				root2 = root2.right

			elif root1.val > root2.val:
				s2.pop()
				root2 = root2.right
				root1 = None
			elif root2.val > root1.val:
				s1.pop()
				root1 = root1.right
				root2 = None
		else:
				break

common_nodes(A, B)