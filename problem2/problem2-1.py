a=[]
e=[]
b=input("Enter number of elements to insert into list")
c=int(b)
for i in range(0,c):
	d=input("Enter element")
	a.append(d)
for i in range(0, len(a)):
	a[i]=int(a[i])
for i in range(0, len(a)):	
	if a[i]<5:
		e.append(a[i])
print(e)