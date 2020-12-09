parent = [-1, 0, 0, 1, 1, 3, 5]

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def createNode(parent, created, i, root):
	if created[i]:
		return

	created[i] = Node(i)
	if parent[i] == -1:
		root[0]  = created[i]
		return

	if created[parent[i]] is None:
		createNode(parent, created, parent[i], root)

	p = created[parent[i]]

	if p.left is None:
		p.left = created[i]
	else:
		p.right = created[i]


def createTree(parent):
	n = len(parent)
	created = [None for i in range(n+1)]
	root = [0]
	for i in range(n):
		createNode(parent, created, i, root)

	return root[0]

print(createTree(parent).left.right.val)