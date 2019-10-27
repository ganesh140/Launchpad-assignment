a=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
f=[]
e=[]
for i in range(0,len(a)): 
        for j in range(i+1,len(a)): 
            if a[i]==a[j] and a[i] not in f: 
                f.append(a[i])
for i in range(0,len(a)): 
	if a[i] not in f:
		e.append(a[i])
e=e+f
e.sort()
print(e)