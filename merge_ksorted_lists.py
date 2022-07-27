class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    temp1 = head1
    temp2 = head2
    dummy = Node(0)
    temp = dummy
    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp.next = temp1
            temp1 = temp1.next
        else:
            temp.next = temp2
            temp2 = temp2.next
        temp = temp.next
    if temp1:
        temp.next = temp1
    elif temp2:
        temp.next = temp2
        
    return dummy.next

def mergeKList(klists):
    ans = klists[0]
    for i in range(1, len(klists)):
        ans = merge(klists[i], ans)
        #printList(ans)
        
    return ans

def mergeKListBS(kLists, l, h):
    m = int((l+h)/2)
    if l >= h:
        return kLists[l]
    ansl = mergeKListBS(kLists, l, m)
    ansr = mergeKListBS(kLists, m+1, h)
    return merge(ansl, ansr)

def createList(arr):
    head = None
    for val in arr:
        if head:
            newNode = Node(val)
            temp.next = newNode
            temp = newNode
        else:
            newNode = Node(val)
            head = newNode
            temp = head
            
    return head

def printList(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

h1 = createList([1,3,5,7])
h2 = createList([2,4,6,8])
h3 = createList([0,9,10,11])

kLists = [h1, h2, h3]

res = mergeKListBS(kLists, 0, len(kLists)-1)
printList(res)
