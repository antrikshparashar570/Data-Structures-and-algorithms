class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(2)
five= Node(1)
six = Node(3)

one.next = two
two.next = three
three.next = four
four.next = five

A = one
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

def is_Palindrome(A):
    slow = A
    fast = A

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow = reverse(slow)

    while slow:
        print(A.val, slow.val)
        if A.val != slow.val:
            return False
        slow = slow.next
        A = A.next

    return True


print(is_Palindrome(A))