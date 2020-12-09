A = [0, 0, 0, 1]
m = 4

start = 0
end = 0

n = len(A)

l = 0
r = 0
maxx = 0
k = 0

while r < n:
    if k <= m:
        if A[r] == 0:
            k += 1
        r += 1        
    if k > m:
        if A[l] == 0:
            k -= 1
        l += 1

    if r-l > maxx:
        start = l
        end = r
        maxx = max(maxx, r-l)

for i in range(start, end):
    if A[i] == 0:
        print(i, end=" ")
