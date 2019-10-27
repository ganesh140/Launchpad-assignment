a=input("Enter the sentence")
b=a.split(" ")
b=b[-1::-1]
for i in range(1,len(b)):
	print(b[0].capitalize()+" "+b[i],end=" ")
#Tried capitalize for no reason and googled how to print without newline(end)