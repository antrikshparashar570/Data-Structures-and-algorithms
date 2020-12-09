def sort_0_1_2(A):
    low = 0
    high = len(A)-1
    mid = 0

    while mid <= high:
        if A[mid] == 0:
            A[mid], A[low] = A[low], A[mid]
            low += 1
            mid += 1
        elif A[mid] == 1:
            mid += 1
        else:
            A[mid], A[high] = A[high], A[mid]
            high -= 1

    return A

A = [2, 2, 2, 1, 0, 1, 0, 2, 0, 1]
print(sort_0_1_2(A))