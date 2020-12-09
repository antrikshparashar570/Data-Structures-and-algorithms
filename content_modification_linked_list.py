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

def middle(A):
	slow = A
	fast = A

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	if fast:
		return slow.next
	else:
		slow

def reverse(A):
	prev = None
	curr = A
	nex = None

	while curr:
		nex = curr.next
		curr.next = prev
		prev = curr
		curr = nex

	return prev

def modify(A):
	mid = middle(A)
	last = reverse(mid)
	temp1 = last
	temp2 = A

	while temp1:
		temp2.val = temp2.val - temp1.val
		temp2 = temp2.next
		temp1 = temp1.next

	temp2.next = reverse(last)

modify(A)

i = A
while i:
	print(i.val)
	i = i.next

