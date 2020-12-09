A = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

i = 0
n = len(A)

for j in range(len(A)):
    if A[j] < 0:
        A[i], A[j] = A[j], A[i]
        i += 1

print(A)

pos, neg = i, 0
while pos < n and neg < pos and A[neg] < 0:
    A[pos], A[neg] = A[neg], A[pos]
    pos += 1
    neg += 2

print(A)