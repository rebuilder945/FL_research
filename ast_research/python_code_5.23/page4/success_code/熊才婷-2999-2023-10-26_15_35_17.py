lst1=input().split()
lst2=input().split()
n=int(lst2[0])
m=int(lst2[1])
x=lst1[n]
y=lst1[m]
lst1[n]=y
lst1[m]=x
i=" ".join(lst1)
print(i.split())
