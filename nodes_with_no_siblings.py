class Node: 
      
    # A constructor to create new tree node 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
  
# Function to print all non-root nodes that don't have 
# a sibling 
def printSingles(root, ans): 
  
    # Base Case 
    if root is None: 
        return 
  
    # If this is an internal node , recur for left 
    # and right subtrees 
    if root.left is not None and root.right is not None: 
        printSingles(root.left, ans) 
        printSingles(root.right, ans) 
  
    # If left child is NULL, and right is not, print 
    # right child and recur for right child 
    elif root.right is not None: 
        ans.append(root.right.key) 
        printSingles(root.right, ans) 
  
    # If right child is NULL and left is not, print 
    # left child and recur for left child 
    elif root.left is not None: 
        ans.append(root.left.key) 
        printSingles(root.left, ans) 

    return ans  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(5) 
root.right.left.left = Node(6) 
print(printSingles(root, []))