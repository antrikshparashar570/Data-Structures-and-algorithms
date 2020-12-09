class Node: 
    def __init__(self, data): 
        self.val = data  
        self.left = self.right = None

root = Node(6)
root.left = Node(8)  
root.right = Node(9)  
root.right.left = Node(7)  
root.right.right = Node(10)  
root.right.right.right = Node(11)

def spiral(A):
	if A is None:
		return None

	ans = []
	q = []
	q.append((root, 0))

	while len(q) > 0:
		node = q.pop(0)
		if len(ans) < node[1]+1:
			ans.append([])

		if node[1]%2 == 0:
			ans[node[1]].insert(0, node[0].val)
		else:
			ans[node[1]].append(node[0].val)

		if node[0].left:
			q.append((node[0].left, node[1]+1))
		if node[0].right:
			q.append((node[0].right, node[1]+1))

	return ans

print(spiral(root))