s = "BBABCBCAB"
n = len(s)

L = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    L[i][i] = 1

j = 0
for g in range(1, n):
    for i in range(n-g):
        j = i+g
        if s[i] == s[j]:
            L[i][j] = L[i+1][j-1] + 2
        else:
            L[i][j] = max(L[i+1][j], L[i][j-1])
    j = 0

for i in range(n):
    print(L[i])
