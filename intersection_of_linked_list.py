class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

Aone = Node(1)
Atwo = Node(2)
Athree = Node(3)
Afour = Node(4)
Afive= Node(6)

A = Aone
Aone.next = Atwo
Atwo.next = Athree
Athree.next = Afour
Afour.next = Afive

Bone = Node(2)
Btwo = Node(4)
Bthree = Node(6)
Bfour = Node(8)

B = Bone

Bone.next = Btwo
Btwo.next = Bthree
Bthree.next = Bfour

def intersection(A, B):
	last_ptr = None
	result = None
	while A and B:
		if A.val == B.val:
			temp = Node(A.val)
			if last_ptr is None:
				last_ptr = temp
				result = last_ptr
			else:
				last_ptr.next = temp
				last_ptr = last_ptr.next
			A = A.next
			B = B.next
		elif A.val < B.val:
			A = A.next
		else:
			B = B.next

	return result

res = intersection(A, B)

while res:
    print(res.val)
    res = res.next