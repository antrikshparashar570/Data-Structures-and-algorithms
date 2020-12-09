A = [ 1, 1, 2, 4, 4, 5, 5, 6, 6, 6 ]

def findElement(A):
    low = 0
    high = len(A)-1

    while low < high:
        mid = int((low+high)/2)

        if mid%2 == 0:
            if A[mid] == A[mid+1]:
                low = mid+2
            else:
                high = mid
        else:
            if A[mid] == A[mid-1]:
                low = mid+1
            else:
                high = mid-1

    return A[low]
 

def onceElement(A):
    print(findElement(A))

onceElement(A)
