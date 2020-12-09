A = [ 5, 2, 1, 3, 2, 6, 8, 8, 8, 6, 6]

def k_most_frequent(A, k):
    n = len(A)
    top = []
    d = {}

    for i in range(n):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    i = 0
    for a,v in (sorted(d.items(), key = lambda item: item[1], reverse=True)):
        top.append(a)
        if i == k-1:
            break
        i += 1
    """i = 0
    print(d)
    for key in d.keys():
        print(key)
        if len(top) < k:
            top.append(key)
        elif len(top) == k and d[top[k]] >= d[key]:
            continue
        else:
            top[k] = d[key]    
        j = len(top)-1

        while j > 0:
            if d[top[j]] > d[top[j-1]]:
                top[j], top[j-1] = top[j-1], top[j]
            else:
                break
            j -= 1"""

    return top

print(k_most_frequent(A, 4))