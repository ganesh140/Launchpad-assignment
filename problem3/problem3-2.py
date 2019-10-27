a=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
f=[]
e=2
for i in range(0,len(a)):
	if e==a[i]:
		f.append(i)
print(f)