A = [2, 4, 6, 8, 9, 10, 12, 13] 
B = [2, 4, 6, 8, 10, 12, 13]

n = min(len(A), len(B))

l = 0
h = n-1
index = n

while l <= h:
    m = int((l+h)/2)

    if A[m] == B[m]:
        l = m+1
    else:
        index = m
        h = m-1

print(index, A[index])