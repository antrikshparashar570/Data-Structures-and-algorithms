A = ["abb", "abc", "xyz", "xyy"]
pat = "mno"

def check(s, pat):
    d1 = {}
    for i in range(len(s)):
        if pat[i] in d1:
            if d1[pat[i]] != s[i]:
                return 
        else:
            d1[pat[i]] = s[i]

    return s

ans = []
for i in range(len(A)):
    if check(A[i], pat) and check(pat, A[i]) != None:
        ans.append(check(A[i], pat))

print(ans)