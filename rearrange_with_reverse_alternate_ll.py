class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

Aone = Node(1)
Atwo = Node(2)
Athree = Node(3)
Afour = Node(4)
#Afive= Node(5)

A = Aone
Aone.next = Atwo
Atwo.next = Athree
Athree.next = Afour
#Afour.next = Afive

def reverse(head):
	curr = head
	prev = None
	nextx = head

	while curr:
		nextx = curr.next
		curr.next = prev
		prev = curr
		curr = nextx

	return prev

def rearrange(A):
	slow = A
	fast = A

	while fast and fast.next:
		last = slow
		slow = slow.next
		fast = fast.next.next

	head2 = None
	if fast:
		head2 = slow.next
		slow.next = None
	else:
		last.next = None
		head2 = slow

	head2 = reverse(head2)

	head1 = A
	
	while head1 and head2:
		nextx1 = head1.next
		nextx2 = head2.next
		head1.next = head2
		head2.next = nextx1
		head1 = nextx1
		head2 = nextx2

	return A

temp = rearrange(A)

while temp:
	print(temp.val)
	temp = temp.next