class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10) 
root.left = Node(2) 
root.right   = Node(10); 
root.left.left  = Node(20); 
root.left.right = Node(1); 
root.right.right = Node(-25); 
root.right.right.left   = Node(3); 
root.right.right.right  = Node(4);

def findMaxUtil(root, res):

    if root is None:
        return 0

    l = findMaxUtil(root.left, res)
    r = findMaxUtil(root.right, res)

    max_single = max(max(l, r) + root.val, root.val)

    max_top = max(max_single, l+r+root.val)

    res[0] = max(max_top, res[0])

    return max_single

def findMax(root):

    res = [-99999]
    findMaxUtil(root, res)
    print(res[0])

findMax(root)