n=int(input())
lst1=[]
for i in range(1,n+1):
    lst1.append(i)
lst2=[]
for x in lst1[1:]:
    lst2.append(x)
lst2.append(lst1[0])
print(lst2)
