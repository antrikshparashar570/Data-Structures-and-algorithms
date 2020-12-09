A = [2, 3, 7, 8, 6, 2, 1]
#A = [10, 90, 49, 2, 1, 5, 23] 

flag = True
for i in range(1,len(A)):
    if i%2 == 1:
        if A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
    else:
        if A[i] > A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]

    flag = bool(1-flag)
print(A)