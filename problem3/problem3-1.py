a=[]
f=[]
b=input("Enter number of elements to insert into list")
c=int(b)
for i in range(0,c):
	d=input("Enter element")
	a.append(d)
e=input("Enter search element")
for i in range(0,c):
	if e==a[i]:
		f.append(i)
print(f)
