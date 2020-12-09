A = [3, 3, 4, 7, 1, 2, 9, 8]

h = {}
ans = []
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        summ = A[i] + A[j]
        if summ in h:
            ans.append(h[summ][0])
            ans.append(h[summ][1])
            ans.append(i)
            ans.append(j)
            break
        else:
            h[summ] = (i, j)

    if len(ans) > 0:
        break

print(ans)