class node:  
      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.data = data  

def sum_tree(Node):
    if Node is None:
        return None
    else:
        toSumTree(Node)
        return Node
  
# Convert a given tree to a tree where  
# every node contains sum of values of  
# nodes in left and right subtrees  
# in the original tree  
def toSumTree(A) : 
      
    # Base case  
    if A is None:
        return 0
    
    old_val = A.data
    A.data = toSumTree(A.left) + toSumTree(A.right)

    return A.data + old_val

  
# A utility function to print  
# inorder traversal of a Binary Tree  
def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.data, end = " ")  
    printInorder(Node.right)  
      
# Utility function to create a new Binary Tree node  
def newNode(data) : 
    temp = node(0)  
    temp.data = data  
    temp.left = None
    temp.right = None
      
    return temp  
  
# Driver Code  
if __name__ == "__main__":  
    root = None
    x = 0
      
    # Constructing tree given in the above figure  
    root = newNode(10)  
    root.left = newNode(-2)  
    root.right = newNode(6)  
    root.left.left = newNode(8)  
    root.left.right = newNode(-4)  
    root.right.left = newNode(7)  
    root.right.right = newNode(5)  
      
    toSumTree(root)  
      
    # Print inorder traversal of the converted  
    # tree to test result of toSumTree()  
    print("Inorder Traversal of the resultant tree is: ")  
    printInorder(root)