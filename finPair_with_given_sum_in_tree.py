class node:      
    def __init__(self, data):  
        self.left = None
        self.right = None
        self.val = data

A = node(15)
A.left = node(10)
A.right = node(20)
A.left.left = node(8)
A.left.right = node(12)
A.right.left = node(16)
A.right.right = node(25)

def findPairUtil(A, s, summ, ans):
	if A is None:
		return
	findPairUtil(A.left, s, summ, ans)
	if summ[0] - A.val in s:
		ans.append(A.val)
		ans.append(summ[0]-A.val)
	else:
		s.add(A.val)
	findPairUtil(A.right, s, summ, ans)

def findPair(A, sum):
	s = set()
	ans = []
	summ = [sum]
	findPairUtil(A, s, summ, ans)
	return ans

print(findPair(A, 28))