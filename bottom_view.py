class newNode:  
      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.val = data 

root = newNode(20)  
root.left = newNode(8)  
root.right = newNode(22)  
root.left.left = newNode(5)  
root.left.right = newNode(3)
root.left.right.left = newNode(10)
root.left.right.right = newNode(14)  
root.right.left = newNode(4)  
root.right.right = newNode(25)

def bottom_view(A, l, h, d):
	if A is None:
		return None

	if l not in d or d[l][1] <= h:
		d[l] = (A.val, h)

	bottom_view(A.left, l-1, h+1, d)
	bottom_view(A.right, l+1, h+1, d)

	return d

def bottom(root):
	if root is None:
		return None
	d = {}
	return bottom_view(root, 0, 0, d)

print(bottom(root))