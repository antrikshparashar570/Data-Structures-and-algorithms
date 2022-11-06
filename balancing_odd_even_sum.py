a = [2, 4, 6, 3, 4]

odd, even = 0, 0
for i in range(len(a)):
	if i%2 == 0:
		odd += a[i]
	
even = sum(a) - odd
l_o, l_e = 0, 0

for i in range(len(a)):
	if i%2 == 0:
		if even - l_e + l_o == odd - l_o - a[i] + l_e:
			print(even - l_e + l_o, odd - a[i])
			print(i, a[i])
			break
		else:
			l_o += a[i]
	else:
		if odd - l_o + l_e == even - l_e - a[i] + l_o:
			print(odd - l_o + l_e,even - a[i] )
			print(i, a[i])
			break
		else:
			l_e += a[i]
			
	
