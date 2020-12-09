class node:      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.val = data

A = node(20)
A.left = node(8)
A.right = node(22)
A.left.left = node(4)
A.left.right = node(12)
A.left.right.left = node(10)
A.left.right.right = node(14)

def kth_smallest(A, k):
	s = []
	node = A
	while True:
		if node:
			s.append(node)
			node = node.left
		else:
			node = s.pop()
			k -= 1
			if k ==0:
				return node.val
			node = node.right

print(kth_smallest(A, 3))