class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

Aone = Node(10)
Atwo = Node(4)
Athree = Node(5)
Afour = Node(3)
Afive= Node(6)

A = Aone
Aone.next = Atwo
Atwo.next = Athree
Athree.next = Afour
Afour.next = Afive

def rearrange(A):
	if A is None:
		return None

	odd = A
	even = A.next

	evenFirst = even

	while 1:
		if odd is None or even is None or even.next is None:
			odd.next = evenFirst
			break

		odd.next = even.next
		odd = even.next

		if odd.next is None:
			even.next = None
			odd.next = evenFirst
			break

		even.next = odd.next
		even = odd.next

	return A

A = rearrange(A)

temp = A
while temp:
	print(temp.val, end = " ")
	temp = temp.next