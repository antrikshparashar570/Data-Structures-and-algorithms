s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9]

class Activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

ans = []
li = []
for i in range(len(s)):
    li.append(Activity(s[i], f[i]))

li = sorted(li, key = lambda item : item.finish)

i = 0
ans.append(li[i])
for j in range(1, len(s)):
    if li[j].start > li[i].finish:
        ans.append(li[j])
        i = j

for i in range(len(ans)):
    print((ans[i].start, ans[i].finish), end = " ")