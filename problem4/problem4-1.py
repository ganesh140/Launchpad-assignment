a=[]
f=[]
e=[]
b=input("Enter number of elements to insert into list")
c=int(b)
for i in range(0,c):
	d=input("Enter element")
	a.append(d)
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