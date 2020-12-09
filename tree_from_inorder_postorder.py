In = [4, 8, 2, 5, 1, 6, 3, 7] 
Post = [8, 4, 5, 2, 6, 7, 3, 1]

class newNode:  
      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.val = data


def tree(In, Post, start, end, pindex):
	if start > end:
		return None

	a = pindex[0]
	node = newNode(Post[a])
	pindex[0] -= 1

	if start == end:
		return node

	index = In.index(node.val)

	node.right = tree(In, Post, index+1, end, pindex[0])
	node.left = tree(In, Post, start, index-1, pindex[0])

	return node

pindex = [len(In)-1]
A = tree(In, Post, 0, len(In)-1, pindex)

print(A.val, A.left.val, A.left.left.val, A.left.left.right.val, A.left.right.val, A.right.val, A.right.left.val, A.right.left.left.val)