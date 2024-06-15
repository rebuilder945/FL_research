lst0=[]
a=input()
while a!='#':
    lst0.append(int(a))
    a=input()
i=len(lst0)
j=sum(lst0)
print(i,j)
